import MathOptInterface as MOI
using HiGHS
using JuMP

model = Model(HiGHS.Optimizer)

# Origins and Destinations
m = 3
n = 4

# Costs
c = [
    80 5 12 15;
    1  9  4  5;
    12 8  6  4
]

# Supply and Demand
supply = [150, 300, 200]
demand = [150, 200, 100, 200]


@variable(model, x[1:m, 1:n] >= 0)


@objective(model, Min,
    sum(c[i,j] * x[i,j] for i in 1:m, j in 1:n))


@constraint(model, [i in 1:m],
    sum(x[i,j] for j in 1:n) == supply[i])

@constraint(model, [j in 1:n],
    sum(x[i,j] for i in 1:m) == demand[j])


optimize!(model)

@assert termination_status(model) == MOI.OPTIMAL

println("Status: ", termination_status(model))

if is_solved_and_feasible(model)
    min_cost = objective_value(model)

    println("Minimum total cost = ", min_cost)

    origins = ["Tabriz", "Yazd", "Kerman"]
    destinations = ["Tehran", "Mashhad", "Isfahan", "Shiraz"]

    for i in 1:m
        for j in 1:n
            println(origins[i], " -> ", destinations[j], " = ", value(x[i,j]))
        end
    end

    @assert isapprox(
        min_cost,
        2550.0;
        atol=1e-6
    )
else
    error("The model is not solved or not feasible.")
end
