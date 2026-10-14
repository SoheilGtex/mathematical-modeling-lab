
# Control Flow in Julia
# =====================
#
# This file demonstrates conditional statements,
# loops, and control flow keywords in Julia.

# 1. IF, ELSEIF, AND ELSE
# -----------------------

score = 17

if score >= 18
    println("Excellent!")
elseif score >= 10
    println("Passed.")
else
    println("Failed.")
end


# 2. COMPARISON OPERATORS
# -----------------------

x = 10
y = 20

if x < y
    println("x is less than y")
end

if x != y
    println("x and y are different")
end


# 3. LOGICAL OPERATORS
# --------------------

age = 21
has_id = true

if age >= 18 && has_id
    println("Access granted.")
end

if age < 18 || !has_id
    println("Access denied.")
end


# 4. FOR LOOPS
# ------------

# Print numbers from 1 to 5
for i in 1:5
    println(i)
end


# 5. WHILE LOOPS
# --------------

function count_to_five()
    counter = 1

    while counter <= 5
        println("Counter: ", counter)
        counter += 1
    end
end

count_to_five()
# Note: Functions are covered in a separate file in this section.


# 6. BREAK
# --------

# Stop the loop when the number reaches 4
for i in 1:10
    if i == 4
        break
    end

    println("Current number: ", i)
end


# 7. CONTINUE
# -----------

# Skip even numbers and print only odd numbers
for i in 1:10
    if i % 2 == 0
        continue
    end

    println("Odd number: ", i)
end


# 8. SHORT-CIRCUIT EVALUATION
# ---------------------------

# Execute the right-hand expression only if the condition is true
temperature = 30

temperature > 25 && println("It is warm.")

temperature < 0 || println("The temperature is not below zero.")


# 9. TERNARY OPERATOR
# -------------------

number = 7

message = number % 2 == 0 ? "Even" : "Odd"

println("The number is ", message)


# 10. PRACTICAL EXAMPLE: PRODUCTION COST
# --------------------------------------

# Calculate production cost based on quantity.
# Total cost = fixed cost + variable cost per unit * quantity

fixed_cost = 1000.0
unit_cost = 25.0
quantity = 40

if quantity < 0
    println("Error: Quantity cannot be negative.")
elseif quantity == 0
    println("No production.")
else
    total_cost = fixed_cost + unit_cost * quantity

    println("Production quantity: ", quantity)
    println("Total production cost: ", total_cost)
end
