#ifndef KV_H
#define KV_H
/* Return the key length of "key=value", or -1 if '=' is missing or the key is
 * empty. `text` must be a non-NULL, NUL-terminated string. */
long kv_key_len(const char *text);
#endif
