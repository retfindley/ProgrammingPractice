#include <stdio.h>
#include <stdlib.h>

void init_array(int *base_address, int size);
void print_array(int *base_address, int size);
void add_element(int *base_address, int index, int value);
int get_element(int *base_address, int index);
void remove_element(int *base_address, int index);

int main(void){

  int size = 5;
  int *base_address = (int*)malloc(size * sizeof(int));

  if (base_address == NULL){
    printf("Memory allocation failed.");
    exit(0);
  }

  /***********Tests***************/

  // Initialize Array
  init_array(base_address, size);
  print_array(base_address, size);

  // Add some stuff to Array
  add_element(base_address, 0, 10);
  add_element(base_address, 1, 11);
  add_element(base_address, 2, -5);
  add_element(base_address, 3, 100000000);
  add_element(base_address, 4, 14);
  print_array(base_address, size);

  // Remove some stuff from init_array
  remove_element(base_address, 2);
  remove_element(base_address, 4);
  print_array(base_address, size);

  // Get some stuff from Array
  int value = 0;
  value = get_element(base_address, 1);
  printf("%d\n", value);
  
  return 0;
}

void init_array(int *base_address, int size){
  for(int i = 0; i < size; i++){
    *(base_address + i) = 0;
  }
}

void print_array(int *base_address, int size){
  for(int i = 0; i < size; i++){
    printf("%d ", *(base_address + i));
  }
  printf("\n");
}
void add_element(int *base_address, int index, int value){
  *(base_address + index) = value;
  return;
}

int get_element(int *base_address, int index){
  return(*(base_address + index));
}

void remove_element(int *base_address, int index){
  *(base_address + index) = 0;
  return;
}
