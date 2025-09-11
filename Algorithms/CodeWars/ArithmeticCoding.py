"""
Arithmetic coding (https://en.wikipedia.org/wiki/Arithmetic_coding) is a data compression technique. In this task we will implement the encoding and decoding functions using rational arithmetic. We will work on strings of lower-case text.

Here is an outline of the encoding algorithm:
Break the source text into a finite set of symbols. In our implementation these will be the letters of the alphabet, in lower-case, plus the space character, and the symbol Z which marks the end of the text.

Create a "model" associating each symbol with a semi-open sub-interval of the unit interval [0, 1). For each symbol, the size of the corresponding sub-interval is in proportion to the probability of that symbol occurring in the source text. For example, a which is one of the most frequently occurring letters in English text might be associated with the interval [0, 0.1) (probability of 10%), whereas b might be associated with the interval [0.1, 0.12) (probability of 2%). The sub-intervals of the model are contiguous and fill the unit interval, so every value 0 <= x < 1 lies in exactly one interval of the model.

For each symbol in the text, select the corresponding interval and then further divide the selected interval into sub-intervals in the same proportions as in the previous step.

When the end of the text is reached, choose a suitably short fraction which lies within the final interval and return it.

Here is an example, using a small set of symbols:
The symbols used are: a, b, c, Z
Let's say that the associated probabilities of these symbols occurring in the text are:
a: 50%
b: 20%
c: 20%
Z: 10%
The corresponding intervals are therefore:
a: [0, 0.5)
b: [0.5, 0.7)
c: [0.7, 0.9)
Z: [0.9, 1)
In this example the text to be encoded is "ac"
We append the end-of-text symbol so our text becomes "acZ":
The first symbol a selects the interval [0, 0.5), so we now subdivide this interval to get:
a: [0, 0.25)
b: [0.25, 0.35)
c: [0.35, 0.45)
Z: [0.45, 0.5)
The second symbol c selects the interval [0.35, 0.45). We subdivide this interval to get:
a: [0.35, 0.4)
b: [0.4, 0.42)
c: [0.42, 0.44)
Z: [0.44, 0.45)
The final symbol Z selects the interval [0.44, 0.45). As this symbol marks the end of the text to be encoded we may stop here and return a value from the interval [0.44, 0.45)
We choose a fraction in the interval which minimises the number of bits in its binary representation. In this case: 0.4453125 which is 0.0111001 in binary
The decoding algorithm
Decoding works by using the same model as the encoding algorithm, successively identifying the interval containing the value being decoded and subdividing that interval in the same way as the encoding algorithm.

Decoding stops when the end-of-text symbol is encountered.

For example, we can decode the value 0.4453125 using the model from the encoding example above:

a: [0, 0.5)
b: [0.5, 0.7)
c: [0.7, 0.9)
Z: [0.9, 1)
This value lies in the interval [0, 0.5), so the first symbol of our decoded text is a and we now subdivide that interval as we did before when encoding:

a: [0, 0.25)
b: [0.25, 0.35)
c: [0.35, 0.45)
Z: [0.45, 0.5)
The value 0.4453125 now lies in the interval [0.35, 0.45), so the second symbol of our decoded text is c and we further subdivide that interval as before:

a: [0.35, 0.4)
b: [0.4, 0.42)
c: [0.42, 0.44)
Z: [0.44, 0.45)
The value 0.4453125 now lies in the interval [0.44, 0.45). This corresponds to the end-of-text symbol Z, so we can stop and return the message "ac"`

The task:
Implement the functions: encode(message, model) and decode(binfrac, model)

In both functions model is a dictionary with keys corresponding to the set of possible symbols, and corresponding values giving the probability (as a percentage) of each symbol occurring in the text. The probabilities are always integers greater than zero and the sum of all probabilities is always 100. The end-of-text symbol is always Z
message is a text string containing only symbols which are in the model
binfrac is a binary string representation of a value in the interval [0, 1)
Notes:
You must preserve the order of symbols given in the dictionary. The first symbol occupies the first (leftmost) sub-interval of the model and so on.
You must append the end-of-text symbol to the message being encoded.
Return the final value of the encoded message as a binary fraction. Always choose a fraction from the final interval which minimises the number of bits in its binary representation. For example, from the interval [0.2, 0.6) choose the binary fraction 0.1 (i.e. decimal 0.5) rather than 0.01 (i.e. decimal 0.25)
Don't implement your functions using double or float types as these have limited precision and rounding errors will occur. You may use Python's fractions module or do rational arithmetic in your own code.
"""

from fractions import Fraction
import math

def build_intervals(model, low=Fraction(0), high=Fraction(1)):
    """Build subintervals [low, high) for each symbol in model (dict order)."""
    total = sum(model.values())
    intervals = {}
    pos = low
    for sym, prob in model.items():
        width = (high - low) * Fraction(prob, total)
        intervals[sym] = (pos, pos + width)
        pos += width
    return intervals

def _to_binary(frac: Fraction) -> str:
    """Convert exact Fraction 0 <= x < 1 into binary string '0.xxx' (terminating for dyadic fractions)."""
    num, den = frac.numerator, frac.denominator
    bits = []
    while num:
        num *= 2
        if num >= den:
            bits.append('1')
            num -= den
        else:
            bits.append('0')
    return "0." + "".join(bits)

def encode(message: str, model: dict) -> str:
    """Arithmetic-encode `message` using `model` and return shortest binary fraction '0.xxx'."""
    message = message + "Z"
    low, high = Fraction(0), Fraction(1)

    for sym in message:
        intervals = build_intervals(model, low, high)
        low, high = intervals[sym]

    # Find smallest k such that exists integer n with:
    #    low <= n / 2^k < high
    k = 1
    while True:
        start = math.ceil(low * 2**k)
        end   = math.ceil(high * 2**k) - 1   # ceil(high*2^k)-1 enforces strict '< high'
        if start <= end:
            frac = Fraction(start, 2**k)     # choose the first valid dyadic in this resolution
            return _to_binary(frac)
        k += 1

def _binstr_to_frac(binstr: str) -> Fraction:
    """Convert '0.xxx' binary string to Fraction."""
    assert binstr.startswith("0."), "binary fraction must be '0.xxx'"
    frac = Fraction(0)
    for i, b in enumerate(binstr.split('.')[1], start=1):
        if b == '1':
            frac += Fraction(1, 2**i)
    return frac

def decode(binfrac: str, model: dict) -> str:
    """Decode binary fraction '0.xxx' back into original message using model."""
    value = _binstr_to_frac(binfrac)
    out = []
    low, high = Fraction(0), Fraction(1)

    while True:
        intervals = build_intervals(model, low, high)
        for sym, (l, h) in intervals.items():
            if l <= value < h:
                if sym == "Z":
                    return "".join(out)
                out.append(sym)
                low, high = l, h
                break
# Example
if __name__ == "__main__":
    model = {'a': 50, 'b': 20, 'c': 20, 'Z': 10}
    msg = "ac"

    enc = encode(msg, model)
    print("Encoded:", enc)   # → 0.0111001

    dec = decode(enc, model)
    print("Decoded:", dec)   # → ac