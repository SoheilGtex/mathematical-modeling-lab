import MathOptInterface as MOI
using JuMP
using HiGHS

model = Model(HiGHS.Optimizer)

@variable(model, x >= 0) # Regular boats
@variable(model, y >= 0) # Competition boats

@objective(model, Max, 50*x + 80*y)

@constraint(model, 50*x + 30*y <= 1000) # Aluminum
@constraint(model, 20*x + 15*y <= 300) # Machine time
@constraint(model, 3*x + 5*y <= 200) # Human labor


optimize!(model)

@assert termination_status(model) == MOI.OPTIMAL

println("Status: ", termination_status(model))

if is_solved_and_feasible(model)
    println("Regular boats = ", value(x))
    println("Competition boats = ", value(y))

    max_profit = objective_value(model)
    println("Maximum profit = ", max_profit)

    @assert isapprox(max_profit, 1600.0; atol=1e-6)
else
    error("The model is not solved or not feasible.")
end
