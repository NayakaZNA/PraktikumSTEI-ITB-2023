module AlternateSort where
-- NOMOR 11
minElmt :: [Int] -> Int
minElmt li
 | length li == 1 = head li
 | head li < minElmt (tail li) = head li
 | otherwise = minElmt (tail li)

hapusCoy :: Int -> [Int] -> [Int]
hapusCoy x li
 | null li = li
 | head li == x = hapusCoy x (tail li)
 | otherwise = head li : hapusCoy x (tail li)
 

urut :: [Int] -> [Int]
urut li
 | length li <= 1 = li
 | head li == minElmt li = head li : urut (tail li)
 | otherwise = urut (tail li ++ [head li])

alternateSort :: [Int] -> [Int]
alternateSort li
 | length li <= 1 = li
 | otherwise = head (urut li) : last ( urut li) : alternateSort (tail (init (urut li)))
