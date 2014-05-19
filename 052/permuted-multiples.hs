import Data.List (sort)

main :: IO ()
main = print $ head [n | n <- [1..], all ((== (sort . show) n) . (sort . show) . (n*)) [1..6]]
