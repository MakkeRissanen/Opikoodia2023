class IRingBell():
  def ringbell(self):
    pass

class RingBigBell(IRingBell):
  def ringbell(self):
    print("Ring big bell, BOING!")

class RingSmallBell(IRingBell):
  def ringbell(self):
    print("Ring small bell, DING!")


class BellRinger():
  def __init__(self):
    self.belllist = []

  def addbell(self,bell):
    if isinstance(bell,IRingBell):
      self.belllist.append(bell)

  def ringbells(self):
    for bell in self.belllist:
      bell.ringbell()

def main():
  big_bell_a = RingBigBell()
  big_bell_b = RingBigBell()
  small_bell_a = RingSmallBell()
  small_bell_b = RingSmallBell()

  BellRinger = BellRinger()
  BellRinger.addbell(big_bell_a)
  BellRinger.addbell(big_bell_b)
  BellRinger.addbell(small_bell_a)
  BellRinger.addbell(small_bell_b)

  BellRinger.ringbells()

if __name__ == "__main__":
  main()

  