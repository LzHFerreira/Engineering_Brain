#include "kv.h"

#include <assert.h>

int main(void) {
  assert(kv_key_len("key=value") == 3);
  assert(kv_key_len("a=b=c") == 1);
  assert(kv_key_len("novalue") == -1);
  assert(kv_key_len("=value") == -1);
  assert(kv_key_len("") == -1);
  return 0;
}
