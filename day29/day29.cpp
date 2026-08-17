#define PyObject_HEAD     PyObject ob_base;
#define PyObject_VAR_HEAD     PyVarObject ob_base;

// 宏定义，包含 上一个、下一个，用于构造双向链表用。(放到refchain链表中时，要用到)
#define _PyObject_HEAD_EXTRA		\
	struct _object *_ob_next;		\
	struct _object *_ob_prev;

typedef struct _object {
	_PyObject_HEAD_EXTRA			// 用于构造双向链表
	Py_ssize_t ob_refcnt;			// 引用计数器
	struct _typeobject *ob_type;	// 数据类型
} PyObject;

typedef struct {
	PyObject ob_base;				// PyObject对象
	Py_ssize_t ob_size;				/* Number of items in variable part, 即: 元素个数 */
} PyVarObject;

// float类型
typedef struct {
	PyObject_HEAD
	double ob_fval;
} PyFloatObject;

// int类型
struct _longobject {
	PyObject_VAR_HEAD
	digit ob_digit[1];
};
/* Long (arbitrary precision) integer object interface */
typedef struct _longobject PyLongObject; /* Revealed in longgintrepr.h */

// list类型
typedef struct {
	PyObject_VAR_HEAD
	PyObject **ob_item;
	Py_ssize_t allocated;
} PyListObject;

// tuple类型
typedef struct {
	PyObject_VAR_HEAD
	PyObject *ob_item[1];
} PyTupleObject;

// dict类型
typedef struct {
	PyObject_HEAD
	py_ssize_t ma_used;
	PyDictKeysObject *ma_keys;
	PyObject **ma_values;
} PyDictObject;