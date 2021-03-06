#include <stdio.h>
#include <stdlib.h>

#define ARRAY_SIZE 5

static void init_array(int *base_address);
static void print_array(int *base_address);
static void check_array_bounds(unsigned int index);
static void add_element(int *base_address, unsigned int index, int value);
static int get_element(int *base_address, unsigned int index);
static void remove_element(int *base_address, unsigned int index);

int main(void){

  int *base_address = (int*)malloc(ARRAY_SIZE * sizeof(int));

  if (base_address == NULL){
    printf("Memory allocation failed.");
    exit(0);
  }

  /***********Tests***************/

  // Initialize Array
  init_array(base_address);
  print_array(base_address);

  // Add some stuff to Array
  add_element(base_address, 0, 10);
  add_element(base_address, 1, 11);
  add_element(base_address, 2, -5);
  add_element(base_address, 3, 100000000);
  add_element(base_address, 4, 14);
  print_array(base_address);

  // Remove some stuff from init_array
  remove_element(base_address, 2);
  remove_element(base_address, 4);
  print_array(base_address);

  // Get some stuff from Array
  int value = 0;
  value = get_element(base_address, 1);
  printf("%d\n", value);

  free(base_address);
  return 0;
}

static void init_array(int *base_address){
  for(int i = 0; i < ARRAY_SIZE; i++){
    *(base_address + i) = 0;
  }
}

static void print_array(int *base_address){
  for(int i = 0; i < ARRAY_SIZE; i++){
    printf("%d ", *(base_address + i));
  }
  printf("\n");
}

static void check_array_bounds(unsigned int index){
  if (index >= ARRAY_SIZE){
    printf("Index %d out of bounds.", index);
    exit(0);
  }
  return;
}

static void add_element(int *base_address, unsigned int index, int value){
  check_array_bounds(index);
  *(base_address + index) = value;
  return;
}

static int get_element(int *base_address, unsigned int index){
  check_array_bounds(index);
  return(*(base_address + index));
}

static void remove_element(int *base_address, unsigned int index){
  check_array_bounds(index);
  *(base_address + index) = 0;
  return;
}
