#!/usr/bin/env clojure
; If p is the perimeter of a right angle triangle with 
; integral length sides, {a,b,c}, there are exactly three 
; solutions for p = 120.
; 
; {20,48,52}, {24,45,51}, {30,40,50}
; 
; For which value of p < 1000, is the number of solutions 
; maximised?
(defn square [n]
  (* n n))

(defn triple? [a b c]
  (and
    (and (> a 0) (> b 0) (> c 0))
    (and (< a b) (< b c))
    (= (+ (square a) (square b)) (square c))))

(defn solutions [limit p]
  (for [a (range 1 (inc limit)) 
        b (range a (inc limit)) 
        c (range b (inc limit))
        :when (and 
                (= (+ a b c) p)
                (triple? a b c))] 
    (list a b c)))

(def s (map #(solutions 1000 %) (range 1 100)))
(println s)
