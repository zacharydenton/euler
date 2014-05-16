import Data.List (sort)

parse :: String -> [String]
parse = words . map replaceComma . filter notQuote where
    replaceComma ',' = ' '
    replaceComma c = c
    notQuote = (/= '"')

alphaIndex :: Char -> Int
alphaIndex c = fromEnum c - 64

alphaScore :: String -> Int
alphaScore = sum . map alphaIndex

totalScore :: [String] -> Int
totalScore names = sum $ zipWith (*) (map alphaScore $ sort names) [1..]

main :: IO ()
main = do
        str <- readFile "/home/zach/code/euler/022/names.txt"
        print $ totalScore $ parse str
