import MathOptInterface as MOI
using JuMP
using HiGHS

model = Model(HiGHS.Optimizer)

@variable(model, x >= 0) # Color
@variable(model, y >= 0) # Black and white

@objective(model, Max, 60*x + 30*y)

@constraint(model, 20*x + 15*y <= 60000)
@constraint(model, x <= 2000)
@constraint(model, y <= 4000)


optimize!(model)

@assert termination_status(model) == MOI.OPTIMAL

println("Status: ", termination_status(model))

if is_solved_and_feasible(model)
    max_profit = objective_value(model)

    println("Maximum profit = ", max_profit)
    println("Color televisions = ", value(x))
    println("Black and white televisions = ", value(y))

    @assert isapprox(
        max_profit,
        160000.0;
        atol=1e-6
    )
else
    error("The model is not solved or not feasible.")
end
