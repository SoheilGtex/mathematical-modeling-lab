import MathOptInterface as MOI
using JuMP
using HiGHS

model = Model(HiGHS.Optimizer)

@variable(model, x >= 0) # Cheese
@variable(model, y >= 0) # Milk
@variable(model, z >= 0) # Eggs

@objective(model, Min, 100*x + 50*y + 40*z)

@constraint(model, x + 4*y + 2*z >= 12) # Vitamin A
@constraint(model, x + 2*y + 3*z >= 14) # Vitamin B


optimize!(model)

@assert termination_status(model) == MOI.OPTIMAL

println("Status: ", termination_status(model))

if is_solved_and_feasible(model)
    println("Cheese = ", value(x))
    println("Milk = ", value(y))
    println("Eggs = ", value(z))

    min_cost = objective_value(model)
    println("Minimum cost = ", min_cost)

    @assert isapprox(min_cost, 210.0; atol=1e-6)
else
    error("The model is not solved or not feasible.")
end
