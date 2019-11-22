;;;======================================================
;;;  Basic Shape Identification
;;;     Type of shapes :
;;;         1. Triangle
;;;             a. Acute Triangle v
;;;             b. Obtuse Triangle v
;;;             c. Right Triangle v
;;;             d. Isosceles Triangle v
;;;                 i.  Right Isosceles Triangle
;;;                 ii. Obtuse Isosceles Triangle
;;;                 iii.Acute Isosceles Triangle
;;;             e. Equilateral Triangle v
;;;         2. Irregular quadrilaterals
;;;             a. Parallelogram v
;;;                 i.  Rhombus
;;;                 ii. Kite
;;;             b. Trapezium
;;;                 i.  Isosceles Trapezium
;;;                 ii. Right Trapezium
;;;                 iii.Left Trapezium
;;;         3. Pentagon v
;;;         4. Hexagon v
;;;     
;;;
;;;======================================================


;;****************
;;* DEFFUNCTIONS *
;;****************

(deffunction ask-question (?question $?allowed-values)
   (printout t ?question)
   (bind ?answer (read))
   (if (lexemep ?answer) 
       then (bind ?answer (lowcase ?answer)))
   (while (not (member ?answer ?allowed-values)) do
      (printout t ?question)
      (bind ?answer (read))
      (if (lexemep ?answer) 
          then (bind ?answer (lowcase ?answer))))
   ?answer)

(deffunction yes-or-no-p (?question)
   (bind ?response (ask-question ?question yes no y n))
   (if (or (eq ?response yes) (eq ?response y))
       then yes 
       else no))


;;*******************************
;;* CHOOSE SHAPE RULES *
;;*******************************

(defrule determine-which-geometric ""
   (not (number-of-vertices ?))
   (not (known ?))
   =>
   (assert (number-of-vertices (ask-question "How many vertices the shape has ?" three four five six )))
)
;;****************
;;* Triangle *
;;****************
(defrule type-of-triangles ""
   (number-of-vertices three)
   (not (known ?))
   =>
   (assert (number-of-same-edges (ask-question "How many equal edges the triangle has ?" two three none)))
)

(defrule type-of-isosceles-triangles ""
   (number-of-vertices three)
   (number-of-same-edges two)
   (not (known ?))
   =>
   (assert (angles-type (ask-question "What angle do the triangle has ?" acute obtuse right)))
)



(defrule type-of-arbitrary-triangle ""
   (number-of-vertices three)
   (number-of-same-edges none)
   (not (known ?))
   =>
   (assert (number-acute-angles (ask-question "Number of acute angle(s) in triangle ?" two three )))
)

(defrule acute-arbitrary-triangle ""
   (number-of-vertices three)
   (number-of-same-edges none)
   (number-acute-angles three)
   (not (known ?))
   =>
   (assert (known " Acute Triangle"))
)

(defrule obtuse-or-right-arbitrary-triangle ""
   (number-of-vertices three)
   (number-of-same-edges none)
   (number-acute-angles two)
   (not (known ?))
   =>
   (assert (number-right-angles (ask-question "Number of right angle in triangle ?" one none)))
)

(defrule right-arbitrary-triangle ""
   (number-of-vertices three)
   (number-of-same-edges none)
   (number-acute-angles two)
   (number-right-angles one)
   (not (known ?))  
   =>
   (assert (known "Right triangle"))
)

(defrule obtuse-arbitrary-triangle ""
   (number-of-vertices three)
   (number-of-same-edges none)
   (number-acute-angles two)
   (number-right-angles none)
   (not (known ?))  
   =>
   (assert (known "Obtuse triangle"))
)
(defrule acute-isosceles-triangles ""
   (number-of-vertices three)
   (number-of-same-edges two)
   (angles-type acute)
   =>
   (assert (known "Isosceles Acute Triangle"))
)
(defrule obtuse-isosceles-triangles ""
   (number-of-vertices three)
   (number-of-same-edges two)
   (angles-type obtuse)
   =>
   (assert (known "Isosceles Obtuse Triangle"))
) 

(defrule right-isosceles-triangles ""
   (number-of-vertices three)
   (number-of-same-edges two)
   (angles-type right)
   =>
   (assert (known "Isosceles Right Triangle"))
) 

(defrule equilateral-triangle ""
   (number-of-vertices three)
   (number-of-same-edges three)
   (not (known ?))  
   =>
   (assert (known "Equilateral triangle"))
)
;;****************
;;* Irregular Quadrilaterals *
;;****************
(defrule type-of-quadrilaterals ""
   (number-of-vertices four)
   (not (known ?))
   =>
   (assert (number-of-parallel (ask-question "How many pair parallel side ?" one two none)))
)
;;****************
;;* Parallelogram *
;;****************
(defrule type-of-parallelogram ""
   (number-of-vertices four)
   (number-of-parallel two)
   (not (known ?))
   =>
   (assert (number-of-congrent-side (ask-question "How many  equal adjacent  edges parallelogram has ?" four two)))
)

(defrule kite-parallelogram ""
   (number-of-vertices four)
   (number-of-parallel two)
   (number-of-congrent-side two)
   (not (known ?))
   =>
   (assert (known "Kite"))
)

(defrule rhombus-parallelogram ""
   (number-of-vertices four)
   (number-of-parallel two)
   (number-of-congrent-side four)
   (not (known ?))
   =>
   (assert (known "Rhombus"))
)

(defrule quadrilaterals ""
   (number-of-vertices four)
   (number-of-parallel none)
   (not (known ?))
   =>
   (assert (known "Quadrilaterals"))
)
;;****************
;;* Trapezoid *
;;****************

(defrule type-of-trapezoid""
   (number-of-vertices four)
   (number-of-parallel one)
   (not (known ?))
   =>
   (assert (is-the-legs-congruent (yes-or-no-p "Does the legs congruent ?")))
)

(defrule isosceles-trapezoid""
   (number-of-vertices four)
   (number-of-parallel one)
   (is-the-legs-congruent yes)
   (not (known ?))
   =>
   (assert (known "Isosceles Trapezium"))
)

(defrule left-right-trapezoid""
   (number-of-vertices four)
   (number-of-parallel one)
   (is-the-legs-congruent no)
   (not (known ?))
   =>
   (assert (right-angle-position(ask-question "Where do the right angle locates ?" right left)))
)

(defrule right-trapezoid""
   (number-of-vertices four)
   (number-of-parallel one)
   (is-the-legs-congruent no)
   (right-angle-position right)
   (not (known ?))
   =>
   (assert (known "Right Trapezium"))
)

(defrule left-trapezoid""
   (number-of-vertices four)
   (number-of-parallel one)
   (is-the-legs-congruent no)
   (right-angle-position left)
   (not (known ?))
   =>
   (assert (known "Left Trapezium"))
)

;;****************
;;* Pentagon *
;;****************
(defrule is-pentagon ""
   (number-of-vertices five)
   (not (known ?))
   =>
   (assert (number-of-same-edges (ask-question "How many equal edges the pentagon has ?" five other)))
)
(defrule regular-pentagon-shape ""
   (number-of-vertices five)
   (number-of-same-edges five)
   (not (known ?))
   =>
   (assert (known "Regular Pentagon"))
)

(defrule irregular-pentagon-shape ""
   (number-of-vertices five)
   (number-of-same-edges other)
   (not (known ?))
   =>
   (assert (known "Irregular Pentagon"))
)

;;****************
;;* Hexagon *
;;****************
(defrule is-hexagon""
   (number-of-vertices six)
   (not (known ?))
   =>
   (assert (number-of-same-edges (ask-question "How many equal edges the hexagon has ?" six other)))
)
(defrule regular-pentagon-shape ""
   (number-of-vertices six)
   (number-of-same-edges six)
   (not (known ?))
   =>
   (assert (known "Regular Hexagon"))
)

(defrule irregular-pentagon-shape ""
   (number-of-vertices six)
   (number-of-same-edges other)
   (not (known ?))
   =>
   (assert (known "Irregular Hexagon"))
)



;;****************
;;* Print Result *
;;****************
(defrule print-result ""
  (declare (salience 10))
  (known ?item)
  =>
  (printout t "Shape:")
  (printout t crlf crlf)
  (format t " %s%n%n%n" ?item))
