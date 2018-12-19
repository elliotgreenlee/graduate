# Winston

This directory contains a modified version of Winston from UTK's CS560 Project 2 with Dr. Cao. It will be used in Sombra for Project 3.

To build the inverted index, run the following commands:

- `python WikiExtractor.py --json -it abbr,b,big,blockquote,center,cite,em,font,h1,h2,h3,h4,hiero,i,kbd,p,plaintext,s,span,strike,strong,tt,u,var ../../data/simplewiki-20170401-pages-meta-current.xml`

Then move the output from wiki extractor to the data directory.

- `./clean_data.py ../../data/text/`
- `number_input.py --i cleaned_pages --o numbered_cleaned_pages`
- `mv numbered_cleaned_pages input`
- `javac -classpath "/hadoop/etc/hadoop:/hadoop/share/hadoop/common/lib/*:/hadoop/share/hadoop/common/*:/hadoop/share/hadoop/hdfs:/hadoop/share/hadoop/hdfs/lib/*:/hadoop/share/hadoop/hdfs/*:/hadoop/share/hadoop/yarn/lib/*:/hadoop/share/hadoop/yarn/*:/hadoop/share/hadoop/mapreduce/lib/*:/hadoop/share/hadoop/mapreduce/*:/contrib/capacity-scheduler/*.jar" -d ./build *.java`
- `jar cvf InvertedIndex.jar *`
- `mkdir output`
- `hadoop jar InvertedIndex.jar elliotjared.programmingassignmenttwo.InvertedIndexBuilder input output`
