parse :: String -> [String]
parse = words . map replaceComma . filter notQuote where
    replaceComma ',' = ' '
    replaceComma c = c
    notQuote = (/= '"')

alphaIndex :: Char -> Int
alphaIndex c = fromEnum c - 64

alphaScore :: String -> Int
alphaScore = sum . map alphaIndex

triangle :: String -> Bool
triangle str = floor t == ceiling t
    where s = alphaScore str
          t = (sqrt (fromIntegral (1 + 8*s)) - 1) / 2

main :: IO ()
main = do
    str <- readFile "/home/zach/code/euler/042/words.txt"
    print $ length $ filter triangle $ parse str
