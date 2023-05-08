ABBREVIATIONS = (
    r'Mr\.', r'Mrs\.', r'Dr\.', r'Lt\.', r'Rep\.', r'B\.A\.', r'Ph\.D\.',
    r'Jan\.', r'Feb\.', r'Mar\.', r'Apr\.', r'Jn\.', r'Jl\.', r'Aug\.', r'Sep\.', r'Oct\.', r'Now\.', r'Dec\.',
    r'Mon\.', r'Tue\.', r'Wed\.', r'Th\.', r'Fr\.', r'Sat\.', r'Sn\.', r'p\.m\.',
    r'ft\.', r'cm\.', r'kg\.', r'g\.',  r'lbs\.', r'in\.', r'sec\.',
    r'etc\.', r'e\.g\.', r'c\.', r'i\.e\.', r'exp\.', r'ex\.', r'vs\.', r'err\.', r'P\.S\.', r'P\.S\.S\.'
)

# REGEX

FILES = r'w+\.w+'                               # dot in the file name
ELLIPSIS = r'\.\.\.'                            # ...
DOUBLE_SIGNS = r"[\?\!|.]{2,}"                  # ?!
NAME = r"[A-Z]\. [A-Z]\. "                      # E. L. Lastname
NUMBERS = r"\b\d+e[+-]\d+|\b\d+[.,]?\d+|\b\d+"
PUNCTUATION = r"[.!?,'\"]"
MATH_SIGNS = r"[/*+=-]"

NUM_SENTENCES = r"[\.?!]"
NUM_NONDECLARE_SENTENCES = r"[!?]"