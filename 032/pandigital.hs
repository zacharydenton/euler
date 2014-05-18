import Data.List (nub, sort)

candidates :: [(String, Integer)]
candidates = [(concatMap show [a, b, a*b], a*b) | a <- [1..2000], b <- [1..50]]

pandigital :: String -> Bool
pandigital = (== "123456789") . sort

main :: IO ()
main = print $ sum $ nub [p | (digits, p) <- candidates, pandigital digits]
