#include "Queue.h"

int main() {
  Queue *q = new ArrayQueue();
  q->add(3);
  q->add(10);
  q->add(5);
  printf("%d\n", q->remove());
  printf("%d\n", q->remove());
  q->add(6);
  q->add(9);
  q->add(12);
  while (!q->isEmpty()) 
    printf("%d\n", q->remove());
}
