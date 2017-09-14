
; all functions are done tail-recursively

; MAIN
(define (mxMul matrix1 matrix2)
  ; if the number of rows of the first matrix is not equal to the columns of
  ;   the second matrix, exit the function (return false). Else, continue...
  (if (not (= (length (car matrix1)) (length matrix2) ))
    #f
    (buildMatrixResult matrix1 (rearrangeSecondMatrix matrix2 '()) '())
  )
)

;	DOT MULTIPLICATION
;		Given two lists of EQUAL NUMBER OF ELEMENTS, get the summation of the
;			products of a pair of index n numbers from the two lists
;   Can be used for matrix multiplication...
(define (dotMultiplicationTail list1 list2 summation)
  ; the length of two lists should be equal for the dot multiplication to work
	(if (not ( = (length list1) (length list2)))
    ; return false if not equal
		#f
    ; do operation if equal
		(if (= (length list1) 0)
			summation
			(dotMultiplicationTail (cdr list1) (cdr list2) (+ summation (* (car list1) (car list2)) ) )
		)
  )
)
(define (dotMul l1 l2) (dotMultiplicationTail l1 l2 0))

; places the resulting rows in the resulting matrix
(define (buildMatrixResult matrix1 matrix2 matrixResult)
  ; this function iterates through the LIST ELEMENTS of the first matrix and initiates dot multiplication
  ;   by using a LIST ELEMENT of the first matrix and the second matrix
	(if (equal? matrix1 '())
		matrixResult
		(buildMatrixResult (cdr matrix1) matrix2 (append matrixResult (list(buildRowResult (car matrix1) matrix2 '())) ) )
    ; (cdr matrix1) iterates through the first matrix until it returns an empty list
    ; (list(buildRowResult (car matrix1) matrix2 '()) ) builds each resulting rows with a list
    ;     from the first matrix and the lists in th second matrix
    ; So, (append matrixResult (list(buildRowResult (car matrix1) matrix2 '()) ) ) appends the row
    ;     with the proper values
	)
)

; places the resulting values from the dot multiplication operation of a list from the first matrix
;   and lists from the second matrix
(define (buildRowResult listOfMatrix1 matrix2 listResult)
  ; this function iterates through the lists of the second matrix
	(if (equal? matrix2 '())
    ; returns the row with the proper values from the dot multiplication operation
		listResult
		(buildRowResult listOfMatrix1 (cdr matrix2) (append listResult (list(dotMul listOfMatrix1 (car matrix2) )) ) )
    ; (cdr matrix2) iterates through the second matrix until it returns an empty list
    ; (list(dotMul listOfMatrix1 (car matrix2) )) gets the resulting value of the dot multiplication
    ;     operation as a list
    ; (append listResult (list(dotMul listOfMatrix1 (car matrix2) )) ) appends the result, in the form
    ;     of a list, into the row list
	)
)

; USED TO TRANSFER THE FIRST INDUVIDUAL ELEMENTS FROM DIFFERENT SUBLIST ROWS INTO ONE LIST
(define (transferFirstElementToNewList listSource listDestination)
	(if (equal? listSource '())
		listDestination
		(transferFirstElementToNewList (cdr listSource) (append listDestination (list(car(car listSource)))) )
	)
)

; USED TO TRANSFER THE REST OF THE SUBLIST ROWS (EXCLUDING THE FIRST ELEMENT) INTO A NEW TEMPORARY MATRIX
(define (transferRestToNewMatrix listSource listDestination)
	(if (equal? listSource '())
		listDestination
		(transferRestToNewMatrix (cdr listSource) (append listDestination (list (cdr (car listSource))) ) )
	)
)

; REARRANGE THE MATRIX IN A WAY ITERATION AND DOT MULTIPLICATION IS POSSIBLE
; example:
; '(  col       '(  row
; r (1 4 7)     c (1 2 3)
; o (2 5 8)  => o (4 5 6)
; w (3 6 9)     l (7 8 9)
; )              )
(define (rearrangeSecondMatrix matrix2 newMatrix)
	; at the end of (transferRestToNewMatrix matrix2 '()), it would return (() () ...)
	; if all of the sublists are empty, then the list is empty
	(if (equal? (car matrix2) '())
		newMatrix
		(rearrangeSecondMatrix (transferRestToNewMatrix matrix2 '()) (append newMatrix (list(transferFirstElementToNewList matrix2 '())) ) )
	)
)

(define g '((1 2 3)	(4 5 6)	(7 8 9)))
(define h	'((1 4 7)	(2 5 8)	(3 6 9)))
