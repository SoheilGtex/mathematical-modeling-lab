# Functions in Julia
# ==================

# This file introduces function definitions, arguments,
# return values, and practical examples for mathematical modeling.


# 1. DEFINING A FUNCTION
# ----------------------

# A function takes inputs, performs an operation, and returns a result.

function add(a, b)
    return a + b
end

println("Sum: ", add(3, 5))


# 2. FUNCTION ARGUMENTS
# ---------------------

# Functions can accept multiple arguments.

function rectangle_area(length, width)
    return length * width
end

println("Rectangle area: ", rectangle_area(4, 6))


# 3. THE RETURN KEYWORD
# ---------------------

# The return keyword specifies the value returned by a function.

function square(x)
    return x^2
end

println("Square: ", square(5))


# 4. IMPLICIT RETURN
# ------------------

# In Julia, the last expression is returned automatically.

function cube(x)
    x^3
end

println("Cube: ", cube(3))


# 5. TYPE-RESTRICTED ARGUMENTS
# ----------------------------

# Argument types can be specified when needed.

function multiply(a::Int, b::Int)
    return a * b
end

println("Product: ", multiply(4, 5))


# 6. FUNCTIONS WITH CONDITIONS
# ----------------------------

# Functions can use conditional statements.

function classify_number(x)
    if x > 0
        return "Positive"
    elseif x < 0
        return "Negative"
    else
        return "Zero"
    end
end

println(classify_number(-3))
println(classify_number(0))
println(classify_number(7))


# 7. FUNCTIONS AND LOOPS
# ----------------------

# Calculate the sum of integers from 1 to n.

function sum_to_n(n)
    total = 0

    for i in 1:n
        total += i
    end

    return total
end

println("Sum from 1 to 100: ", sum_to_n(100))


# 8. A MATHEMATICAL MODELING EXAMPLE
# ---------------------------------

# Total production cost = fixed cost + unit cost * quantity

function production_cost(fixed_cost, unit_cost, quantity)
    if quantity < 0
        error("Quantity cannot be negative.")
    end

    return fixed_cost + unit_cost * quantity
end

cost = production_cost(1000.0, 25.0, 40)

println("Total production cost: ", cost)


# 9. FUNCTION COMPOSITION
# -----------------------

# The output of one function can be used as the input of another.

function double(x)
    return 2 * x
end

function add_one(x)
    return x + 1
end

println("Composed result: ", add_one(double(5)))