main :: IO ()
main = print $ foldr (+) 1 [4*n^2 - 6*n + 6 | n <- [3,5..1001]]
