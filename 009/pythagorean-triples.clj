#!/usr/bin/env clojure
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
