# Beginning MicroPython with the Raspberry Pi Pico: Build Electronics and IoT Projects
# Chapter 3
# https://ontarioskillsoft.percipio.com/books/6c20be20-135b-44fb-afc7-7f65ed8d93c0#epubcfi(/6/40!/4/2%5Bepubmain%5D/2%5Bch03lev1sec1%5D/14%5Bch03lev2sec4%5D/10/1:125)

a = 42
b = 1.5
c = "seventy"

print(
    "{0} {1} {2} {3}"
        .format(
            a,
            b,
            c,
            (2+3)
        )
)

print(
    "{a_var} {b_var} {c_var} {0}"
        .format(
            (3*3),
            c_var=c,
            b_var=b,
            a_var=a
        )
)
