/*
 *  pagerank.scala
 *
 *  Apache Spark implementation of PageRank in Scala on the Simple Wikipedia Page Dump.
 * 
 * Authors: Jared M. Smith and Elliot Greenlee
 */

import org.apache.spark.graphx._
import org.apache.spark.rdd.RDD
import java.io._

// Build the SQLContext needed by Spark to use DataFrames
val sqlContext = new org.apache.spark.sql.SQLContext(sc)

// Define the regular expression to scrape from the pagelinks Wikipedia MariaDB dump
val pagelinksPattern = "\\((\\d*),0,'([^,]*?)',0\\)+[,|;]".r

// Define the regular expression to scrape from the page Wikipedia MariaDB dump
val pagePattern = "\\((\\d*),0,'([^,]*?)','.*?\\)+[,|;]".r


// Define a function to write to a file with Java's Standard library
def printToFile(f: java.io.File)(op: java.io.PrintWriter => Unit) {
  val p = new java.io.PrintWriter(f)
  try { op(p) } finally { p.close() }
}

// Get the start time
val timestampStart: Long = System.currentTimeMillis

// Load the textFiles as RDD. Spark will auto-partition
val page: RDD[String] = sc.textFile("simplewiki-20170401-page.sql")
val pagelink: RDD[String] = sc.textFile("simplewiki-20170401-pagelinks.sql")

// Extract the page data into the pageRDD
// Gets matches in the form of: "page_title","page_id"
val pageRDD: RDD[(String, Long)] = page.flatMap { line =>
  val matches = pagePattern.findAllMatchIn(line).toArray
    matches.map { d =>
        (d.group(2), d.group(1).toLong)
   }
}

// Extract the pagelink data into the pagelinksRDD
// Gets the matches in the form of: "pl_title","pl_from"
val pagelinksRDD: RDD[(String, Long)] = pagelink.flatMap { line =>
  val matches = pagelinksPattern.findAllMatchIn(line).toArray
    matches.map { d =>
        (d.group(2), d.group(1).toLong)
    }
}

// Show number of records in each RDD
println(s"pageRDD: "+pageRDD.count())
println(s"pagelinksRDD: "+pagelinksRDD.count())

// Convert the pageRDD and pagelinksRDD to DataFrames and register them with the sqlContext
pageRDD.toDF("page_title","page_id").registerTempTable("page")
pagelinksRDD.toDF("pl_title","pl_from").registerTempTable("pagelinks")

// Get a DataFrame of Page links using an SQL INNER JOIN
val pagelinksDF = sqlContext.sql("SELECT pagelinks.pl_from as srcId, page.page_id as tgtId, 0 as attr FROM pagelinks INNER JOIN page ON pagelinks.pl_title = page.page_title")

// Build the edges of the graph of pages
// This will be used by Spark and the GraphX library
val edges = pagelinksDF.map { pagelink =>
    Edge(pagelink.getLong(0), pagelink.getLong(1), pagelink.getInt(2))
}.rdd

// Convert the pageRDD to the Vertex class
// This will also be used by Spark and the GraphX library
val vertices = pageRDD.map { d =>
    (d._2, d._1)
}

// Build a graph using Apache Spark's GraphX library
val graph = Graph(vertices, edges, "")

// Run the built-in PageRank algorithm on the Graph
val prGraph = graph.pageRank(0.001)

// Get the graph in a form where we have the titles of the articles as well
val titleAndPrGraph = graph.outerJoinVertices(prGraph.vertices) {
      (v, title, rank) => (rank.getOrElse(0.0), title)
}

// We're done!

// Get the end time of the script
val timestampEnd: Long = System.currentTimeMillis
val duration: Long = timestampEnd - timestampStart
println(s"Duration: $duration ms (~" + duration/1000/60 + " minutes)")

// Print out the top 10 highest weighted pages
titleAndPrGraph.vertices.top(10) {
      Ordering.by((entry: (VertexId, (Double, String))) => entry._2._1)
}.foreach(t => println(t._2._2 + ": " + t._2._1))

// Save this run to a timestamped file
printToFile(new File("pagerank-" + duration/1000 + "-seconds")) { p => 
  titleAndPrGraph.vertices.top(100000000) {
        Ordering.by((entry: (VertexId, (Double, String))) => entry._2._1)
  }.foreach(t => p.println(t._2._2 + ": " + t._2._1))
}
