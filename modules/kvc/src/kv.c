#include "kv.h"

#include <string.h>

long kv_key_len(const char *text) {
  const char *eq = strchr(text, '=');
  return (eq == NULL || eq == text) ? -1 : (long)(eq - text);
}
