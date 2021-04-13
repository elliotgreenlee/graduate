#include <stdlib.h>

struct queue
 {
  void **items;
  int next_free;
  int next_full;
  int max_items;
  int size;
};

void *queue_new(int num_items) {
  struct queue *q = (struct queue *)malloc(sizeof(struct queue));
  q->items = (void **)malloc(sizeof(void *)*num_items);

  q->max_items = num_items;
  q->next_free = 0;
  q->next_full = 0;
  return (void *)q;
}

void queue_enqueue(void *q, void *item) {
  struct queue *myQueue = (struct queue *)q;
  myQueue->items[myQueue->next_free] = item;
  myQueue->next_free = (myQueue->next_free + 1) % myQueue->max_items;
  myQueue->size++;
}

void *queue_dequeue(void *q) {
  struct queue *myQueue = (struct queue *)q;
  void *returnValue = myQueue->items[myQueue->next_full];
  myQueue->next_full = (myQueue->next_full + 1) % myQueue->max_items;
  myQueue->size--;
  return returnValue;
}

int queue_isEmpty(void *q) {
  struct queue *myQueue = (struct queue *)q;
  return (myQueue->size == 0);
}
