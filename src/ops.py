import numpy
class val:
  
  def __init__(self, data, _children=(), _op='', label=''):
    self.data = data
    self.grad = 0.0
    self._backward = lambda: None
    self._prev = set(_children)
    self._op = _op
    self.label = label

  def __repr__(self):
    return f"Value(data={self.data})"
  
  def __add__(self, other):
    out = val(self.data + other.data, (self, other), '+')
    
    def _backward():
      self.grad += 1.0 * out.grad
      other.grad += 1.0 * out.grad
    out._backward = _backward
    
    return out

  def __mul__(self, other):
    out = val(self.data * other.data, (self, other), '*')
    
    def _backward():
      self.grad += other.data * out.grad
      other.grad += self.data * out.grad
    out._backward = _backward
      
    return out

  def __sub__(self, other):
    out = val(self.data - other.data, (self, other), '-')
    
    def _backward():
      self.grad += other.data - out.grad
      other.grad += self.data - out.grad
    out._backward = _backward
      
    return out

  def __truediv__(self, other):
    out = val(self.data / other.data, (self, other), '/')
    
    def _backward():
      self.grad += other.data - out.grad
      other.grad += self.data - out.grad
    out._backward = _backward
      
    return out

  def __pow__(self, other):
    out = val(self.data ** other.data, (self, other), '**')
    
    def _backward():
      self.grad += other.data ** out.grad
      other.grad += self.data ** out.grad
    out._backward = _backward
      
    return out
