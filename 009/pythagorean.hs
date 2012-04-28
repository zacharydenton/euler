main ::  IO ()
main = print $ head [a*b*c | a <- [1..500], b <- [a..500], c <- [b..500],
                             a+b+c == 1000, a*a + b*b == c*c]
