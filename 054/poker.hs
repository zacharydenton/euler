import Data.Char (digitToInt)
import Data.List (nub, sortBy)

rankValue :: Char -> Int
rankValue 'A' = 14
rankValue 'K' = 13
rankValue 'Q' = 12
rankValue 'J' = 11
rankValue 'T' = 10
rankValue  c  = digitToInt c

parse :: String -> [([(Int, Char)], [(Int, Char)])]
parse str = [(parse' left, parse' right) | line <- lines str,
                                           let cards = words line,
                                           let (left, right) = splitAt 5 cards]
    where parse' cards = [(rankValue (head card), last card) | card <- cards]

count :: Eq a => a -> [a] -> Int
count x xs = length $ filter (== x) xs

evaluate :: [(Int, Char)] -> [Int]
evaluate hand | straight && flush           = 9 : ranks
              | k 4                         = 8 : kind 4 ++ kind 1
              | k 3 && k 2                  = 7 : kind 3 ++ kind 2
              | flush                       = 6 : ranks
              | straight                    = 5 : ranks
              | k 3                         = 4 : kind 3 ++ ranks
              | k 2 && k' 2 [head (kind 2)] = 3 : kind 2 ++ kind' 2 [head (kind 2)] ++ ranks
              | k 2                         = 2 : kind 2 ++ ranks
              | otherwise                   = 1 : ranks
              where (r, suits) = unzip hand
                    ranks = sortBy (flip compare) r
                    flush = length (nub suits) == 1
                    straight = (maximum ranks) - (minimum ranks) == 4 && length (nub ranks) == 5
                    kind' n except = [rank | rank <- ranks, count rank ranks == n, rank `notElem` except]
                    kind n = kind' n []
                    k' n except = not $ null $ kind' n except
                    k n = k' n []

main :: IO ()
main = do
    str <- readFile "/home/zach/code/euler/054/poker.txt"
    let games = parse str
    print $ length [left | (left, right) <- games, evaluate left > evaluate right]
