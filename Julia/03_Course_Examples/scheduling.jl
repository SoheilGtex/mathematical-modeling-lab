import MathOptInterface as MOI
using JuMP
using HiGHS

model = Model(HiGHS.Optimizer)

@variable(model, x[1:3, 1:4] >= 0)

c = [
    4 4 5 7;
    6 7 5 6;
    12 10 8 11
]

@objective(model, Min, 
    sum(c[i,j] * x[i,j] for i in 1:3, j in 1:4))

production_min = [3000, 6000, 4000]

@constraint(model, [i in 1:3], 
    sum(x[i,j] for j in 1:4) >= production_min[i])

time_limit = [1500, 1200, 1500, 2000]
    
a = [
    0.3 0.25 0.2 0.2;
    0.2 0.3 0.2 0.25;
    0.8 0.6 0.6 0.5
]
@constraint(model, [j in 1:4], sum(a[i,j] * x[i,j] for i in 1:3) <= time_limit[j])


optimize!(model)

@assert termination_status(model) == MOI.OPTIMAL

println("Status: ", termination_status(model))

if is_solved_and_feasible(model)
    min_cost = objective_value(model)

    println("Minimum cost = ", min_cost)

    for i in 1:3
        for j in 1:4
            println("Product $i on Machine $j = ", value(x[i,j]))
        end
    end

    @assert isapprox(
        min_cost,
        82500.0;
        atol=1e-6
    )
else
    error("The model is not solved or not feasible.")
end
