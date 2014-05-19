import Data.List (nub)

expand :: Int -> String -> [String]
expand x "" = [s | n <- [100..999], n `rem` x == 0, let s = show n, s == nub s]
expand x s = [c:s | c <- ['0'..'9'], c `notElem` s, (read (c:take 2 s)) `rem` x == 0]

candidates :: [String]
candidates = inner [17, 13, 11, 7, 5, 3, 2, 1] [""] where
    inner [] acc = acc
    inner (x:xs) acc = inner xs $ concatMap (expand x) acc

main :: IO ()
main = print $ sum $ map read candidates
