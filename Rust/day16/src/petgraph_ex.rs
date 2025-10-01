use petgraph::dot::Dot;
use petgraph::graph::UnGraph;
use petgraph::visit::EdgeRef;

pub fn main() {
    // Create an undirected graph with city names as node data and their distances as edge data.
    let mut g = UnGraph::<String, u32>::new_undirected();

    let ber = g.add_node("Berlin".to_owned());
    let del = g.add_node("New Delhi".to_owned());
    let mex = g.add_node("Mexico City".to_owned());
    let syd = g.add_node("Sydney".to_owned());

    // Add distances in kilometers as edge data.
    g.extend_with_edges(&[
        (ber, del, 6_000),
        (ber, mex, 10_000),
        (ber, syd, 16_000),
        (del, mex, 14_000),
        (del, syd, 12_000),
        (mex, syd, 15_000),
    ]);

    // Basic DOT export with automatic labels
    let basic_dot = Dot::new(&g);
    println!("Basic DOT format:\n{:?}\n", basic_dot);
    // Output:
    // Basic DOT format:
    // graph {
    //     0 [ label = "\"Berlin\"" ]
    //     1 [ label = "\"New Delhi\"" ]
    //     2 [ label = "\"Mexico City\"" ]
    //     3 [ label = "\"Sydney\"" ]
    //     0 -- 1 [ label = "6000" ]
    //     0 -- 2 [ label = "10000" ]
    //     0 -- 3 [ label = "16000" ]
    //     1 -- 2 [ label = "14000" ]
    //     1 -- 3 [ label = "12000" ]
    //     2 -- 3 [ label = "15000" ]
    // }

    // Enhanced DOT export with custom attributes
    let fancy_dot = Dot::with_attr_getters(
        &g,
        // Global graph attributes
        &[],
        // Edge attribute getter
        &|graph_reference, edge_reference| {
            // Style edges depending on distance
            if graph_reference.edge_weight(edge_reference.id()).unwrap() > &12_500 {
                "style=dashed, penwidth=3".to_owned()
            } else {
                "style=solid".to_owned()
            }
        },
        // Node attribute getter; We don't change any node attributes
        &|_, (_, _)| String::new(),
    );

    println!("Enhanced DOT format:\n{:?}", fancy_dot);
    // Output:
    // Enhanced DOT format:
    // graph {
    //     0 [ label = "\"Berlin\"" ]
    //     1 [ label = "\"New Delhi\"" ]
    //     2 [ label = "\"Mexico City\"" ]
    //     3 [ label = "\"Sydney\"" ]
    //     0 -- 1 [ label = "6000" style=solid]
    //     0 -- 2 [ label = "10000" style=solid]
    //     0 -- 3 [ label = "16000" style=dashed, penwidth=3]
    //     1 -- 2 [ label = "14000" style=dashed, penwidth=3]
    //     1 -- 3 [ label = "12000" style=solid]
    //     2 -- 3 [ label = "15000" style=dashed, penwidth=3]
    // }

    // This would typically be written to a file:
    // std::fs::write("flight_network.dot", format!("{:?}", fancy_dot)).unwrap();
}
