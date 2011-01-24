#!/usr/bin/env clojure
; A Pythagorean triplet is a set of three natural numbers, a < b < c, 
; for which,
;
; a^(2) + b^(2) = c^(2)
;
; For example, 3^(2) + 4^(2) = 9 + 16 = 25 = 5^(2).
;
; There exists exactly one Pythagorean triplet for which a + b + c = 1000.
; Find the product abc.
(defn square [n]
  (* n n))

(defn triple? [a b c]
  (and
    (and (> a 0) (> b 0) (> c 0))
    (and (< a b) (< b c))
    (= (+ (square a) (square b)) (square c))))

(defn euler [m n]
  (vector
    (- (square m) (square n)) 
    (* 2 m n) 
    (+ (square m) (square n))))

(defn combine [lst1 lst2]
  (mapcat (fn [x] (map #(list % x) lst1)) lst2))


(defn candidates [limit]
  (for [a (range 1 (inc limit)) 
        b (range a (inc limit)) 
        c (range b (inc limit))
        :when (and 
                (= (+ a b c) 1000)
                (triple? a b c))] 
    (list a b c)))
(println (apply * (first (candidates 500))))
