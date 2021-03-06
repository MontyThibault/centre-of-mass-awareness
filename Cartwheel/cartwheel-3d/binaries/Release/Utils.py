# This file was automatically generated by SWIG (http://www.swig.org).
# Version 1.3.39
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.
# This file is compatible with both classic and new-style classes.

from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_Utils', [dirname(__file__)])
        except ImportError:
            import _Utils
            return _Utils
        if fp is not None:
            try:
                _mod = imp.load_module('_Utils', fp, pathname, description)
            finally:
                fp.close()
                return _mod
    _Utils = swig_import_helper()
    del swig_import_helper
else:
    import _Utils
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


try:
    import weakref
    weakref_proxy = weakref.proxy
except:
    weakref_proxy = lambda x: x


class SwigPyIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __swig_destroy__ = _Utils.delete_SwigPyIterator
    __del__ = lambda self : None;
    def value(self): return _Utils.SwigPyIterator_value(self)
    def incr(self, n = 1): return _Utils.SwigPyIterator_incr(self, n)
    def decr(self, n = 1): return _Utils.SwigPyIterator_decr(self, n)
    def distance(self, *args): return _Utils.SwigPyIterator_distance(self, *args)
    def equal(self, *args): return _Utils.SwigPyIterator_equal(self, *args)
    def copy(self): return _Utils.SwigPyIterator_copy(self)
    def next(self): return _Utils.SwigPyIterator_next(self)
    def __next__(self): return _Utils.SwigPyIterator___next__(self)
    def previous(self): return _Utils.SwigPyIterator_previous(self)
    def advance(self, *args): return _Utils.SwigPyIterator_advance(self, *args)
    def __eq__(self, *args): return _Utils.SwigPyIterator___eq__(self, *args)
    def __ne__(self, *args): return _Utils.SwigPyIterator___ne__(self, *args)
    def __iadd__(self, *args): return _Utils.SwigPyIterator___iadd__(self, *args)
    def __isub__(self, *args): return _Utils.SwigPyIterator___isub__(self, *args)
    def __add__(self, *args): return _Utils.SwigPyIterator___add__(self, *args)
    def __sub__(self, *args): return _Utils.SwigPyIterator___sub__(self, *args)
    def __iter__(self): return self
SwigPyIterator_swigregister = _Utils.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)


def tprintf(*args):
  return _Utils.tprintf(*args)
tprintf = _Utils.tprintf

def tvprintf(*args):
  return _Utils.tvprintf(*args)
tvprintf = _Utils.tvprintf

def registerPrintFunction(*args):
  return _Utils.registerPrintFunction(*args)
registerPrintFunction = _Utils.registerPrintFunction

def throwError(*args):
  return _Utils.throwError(*args)
throwError = _Utils.throwError

def readDoublesFromFile(*args):
  return _Utils.readDoublesFromFile(*args)
readDoublesFromFile = _Utils.readDoublesFromFile

def lTrim(*args):
  return _Utils.lTrim(*args)
lTrim = _Utils.lTrim

def rTrim(*args):
  return _Utils.rTrim(*args)
rTrim = _Utils.rTrim

def trim(*args):
  return _Utils.trim(*args)
trim = _Utils.trim

def readValidLine(*args):
  return _Utils.readValidLine(*args)
readValidLine = _Utils.readValidLine

def getTokens(*args):
  return _Utils.getTokens(*args)
getTokens = _Utils.getTokens
class Observer(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Observer, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Observer, name)
    __repr__ = _swig_repr
    def __init__(self): 
        if self.__class__ == Observer:
            _self = None
        else:
            _self = self
        this = _Utils.new_Observer(_self, )
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _Utils.delete_Observer
    __del__ = lambda self : None;
    def update(self, data = None): return _Utils.Observer_update(self, data)
    def __disown__(self):
        self.this.disown()
        _Utils.disown_Observer(self)
        return weakref_proxy(self)
Observer_swigregister = _Utils.Observer_swigregister
Observer_swigregister(Observer)

class Observable(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Observable, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Observable, name)
    __repr__ = _swig_repr
    def __init__(self): 
        this = _Utils.new_Observable()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _Utils.delete_Observable
    __del__ = lambda self : None;
    def hasChanged(self): return _Utils.Observable_hasChanged(self)
    def isDoingBatchChanges(self): return _Utils.Observable_isDoingBatchChanges(self)
    def beginBatchChanges(self): return _Utils.Observable_beginBatchChanges(self)
    def endBatchChanges(self): return _Utils.Observable_endBatchChanges(self)
    def addObserver(self, *args): return _Utils.Observable_addObserver(self, *args)
    def deleteObserver(self, *args): return _Utils.Observable_deleteObserver(self, *args)
    def countObservers(self): return _Utils.Observable_countObservers(self)
    def typeName(self): return _Utils.Observable_typeName(self)
Observable_swigregister = _Utils.Observable_swigregister
Observable_swigregister(Observable)

class DynamicArrayDouble(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, DynamicArrayDouble, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, DynamicArrayDouble, name)
    __repr__ = _swig_repr
    def iterator(self): return _Utils.DynamicArrayDouble_iterator(self)
    def __iter__(self): return self.iterator()
    def __nonzero__(self): return _Utils.DynamicArrayDouble___nonzero__(self)
    def __bool__(self): return _Utils.DynamicArrayDouble___bool__(self)
    def __len__(self): return _Utils.DynamicArrayDouble___len__(self)
    def pop(self): return _Utils.DynamicArrayDouble_pop(self)
    def __getslice__(self, *args): return _Utils.DynamicArrayDouble___getslice__(self, *args)
    def __setslice__(self, *args): return _Utils.DynamicArrayDouble___setslice__(self, *args)
    def __delslice__(self, *args): return _Utils.DynamicArrayDouble___delslice__(self, *args)
    def __delitem__(self, *args): return _Utils.DynamicArrayDouble___delitem__(self, *args)
    def __getitem__(self, *args): return _Utils.DynamicArrayDouble___getitem__(self, *args)
    def __setitem__(self, *args): return _Utils.DynamicArrayDouble___setitem__(self, *args)
    def append(self, *args): return _Utils.DynamicArrayDouble_append(self, *args)
    def empty(self): return _Utils.DynamicArrayDouble_empty(self)
    def size(self): return _Utils.DynamicArrayDouble_size(self)
    def clear(self): return _Utils.DynamicArrayDouble_clear(self)
    def swap(self, *args): return _Utils.DynamicArrayDouble_swap(self, *args)
    def get_allocator(self): return _Utils.DynamicArrayDouble_get_allocator(self)
    def begin(self): return _Utils.DynamicArrayDouble_begin(self)
    def end(self): return _Utils.DynamicArrayDouble_end(self)
    def rbegin(self): return _Utils.DynamicArrayDouble_rbegin(self)
    def rend(self): return _Utils.DynamicArrayDouble_rend(self)
    def pop_back(self): return _Utils.DynamicArrayDouble_pop_back(self)
    def erase(self, *args): return _Utils.DynamicArrayDouble_erase(self, *args)
    def __init__(self, *args): 
        this = _Utils.new_DynamicArrayDouble(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(self, *args): return _Utils.DynamicArrayDouble_push_back(self, *args)
    def front(self): return _Utils.DynamicArrayDouble_front(self)
    def back(self): return _Utils.DynamicArrayDouble_back(self)
    def assign(self, *args): return _Utils.DynamicArrayDouble_assign(self, *args)
    def resize(self, *args): return _Utils.DynamicArrayDouble_resize(self, *args)
    def insert(self, *args): return _Utils.DynamicArrayDouble_insert(self, *args)
    def reserve(self, *args): return _Utils.DynamicArrayDouble_reserve(self, *args)
    def capacity(self): return _Utils.DynamicArrayDouble_capacity(self)
    __swig_destroy__ = _Utils.delete_DynamicArrayDouble
    __del__ = lambda self : None;
DynamicArrayDouble_swigregister = _Utils.DynamicArrayDouble_swigregister
DynamicArrayDouble_swigregister(DynamicArrayDouble)



