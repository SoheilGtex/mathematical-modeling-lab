import MathOptInterface as MOI
using JuMP
using HiGHS


model = Model(HiGHS.Optimizer)

@variable(model, x[1:4] >= 0)
@variable(model, y[1:3] >= 0)

@objective(model, Min,
    20 * (0.07 * x[1] + 0.06 * x[2] + 0.065 * x[3] + 0.075 * x[4]))

@constraint(model, x[1] - y[1] == 2)
@constraint(model, x[2] + 1.06 * y[1] - y[2] == 4)
@constraint(model, x[3] + 1.055 * y[2] - y[3] == 8)
@constraint(model, x[4] + 1.045 * y[3] == 5)


optimize!(model)

@assert termination_status(model) == MOI.OPTIMAL

println("Termination status: ", termination_status(model))

if is_solved_and_feasible(model)
    min_cost = objective_value(model)

    println("Minimum total interest cost: ", min_cost)

    for i in 1:4
        println("Bonds sold in year $i: ", value(x[i]))
    end

    for i in 1:3
        println("Short-term deposit in year $i: ", value(y[i]))
    end

    @assert isapprox(
        min_cost,
        22.1418263452686;
        atol=1e-6
    )
else
    error("The model is not solved or not feasible.")
end
