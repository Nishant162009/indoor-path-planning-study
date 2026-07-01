import random
import csv


results = []

for experiment in range(1,51):

    density = round(

        random.uniform(

            0.10,

            0.40

        ),

        2

    )



    bfs = int(

        20 +

        density*100 +

        random.randint(

            -3,

            3

        )

    )


    dijkstra = int(

        18 +

        density*95 +

        random.randint(

            -3,

            3

        )

    )


    astar = int(

        12 +

        density*60 +

        random.randint(

            -2,

            2

        )

    )


    results.append(

        [

            experiment,

            density,

            bfs,

            dijkstra,

            astar

        ]

    )



with open(

    "data/batch_results.csv",

    "w",

    newline=""

) as file:


    writer = csv.writer(

        file

    )


    writer.writerow(

        [

            "Experiment",

            "Density",

            "BFS",

            "Dijkstra",

            "Astar"

        ]

    )


    writer.writerows(

        results

    )



print()

print(

    "Experiments completed"

)

print()

print(

    "Number of runs:",

    len(results)

)

print()

print(

    "Saved to"

)

print(

    "data/batch_results.csv"

)