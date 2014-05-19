champernowne :: String
champernowne = foldr (\x acc -> (show x) ++ acc) "" [1..]

main :: IO ()
main = print $ product [read [champernowne !! (n - 1)] | n <- [10^x | x <- [0..6]]]
