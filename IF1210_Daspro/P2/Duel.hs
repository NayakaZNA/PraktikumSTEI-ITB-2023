module Duel where
-- NOMOR 7
duel :: [String] -> [String]
duel li
 | null li = [] 
 | head li /= "desperado" = (head li) : duel (tail li) 
 | otherwise = "BANG" : duel (tail li)
