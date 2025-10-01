use petgraph::{
    Undirected,
    algo::astar,
    dot::Dot,
    prelude::{GraphMap, UnGraphMap},
    visit::EdgeRef,
};
use std::fs;

#[derive(Debug, Copy, Clone, Eq, PartialEq, Ord, PartialOrd, Hash)]
struct Pos {
    x: usize,
    y: usize,
}
impl Pos {
    pub fn disp(&self) -> Pos {
        return Pos {
            x: self.x + 1,
            y: self.y + 1,
        };
    }
}

const CW: [isize; 4] = [0, 1, 0, -1];

struct Info {
    start: Pos,
    end: Pos,
    walls: Vec<Vec<bool>>,
}

fn main() {
    let file_path = "src/test.txt";
    let file = fs::read_to_string(file_path).expect("failed to read file");
    let data = file.trim().split("\n").collect::<Vec<&str>>();
    //println!("{:?}", data);

    let mut start: Pos = Pos { x: 0, y: 0 };
    let mut end: Pos = Pos { x: 0, y: 0 };
    for (pos, line) in data.iter().enumerate() {
        if line.contains("S") {
            start = Pos {
                x: line.find("S").unwrap(),
                y: pos,
            };
        } else if line.contains("E") {
            end = Pos {
                x: line.find("E").unwrap(),
                y: pos,
            };
        }
    }

    let walls = data
        .iter()
        .map(|x| {
            x.chars()
                .collect::<Vec<char>>()
                .iter()
                .map(|y| y.eq(&'#'))
                .collect()
        })
        .collect::<Vec<Vec<bool>>>();
    //println!("Walls: {:?}", walls);

    let mut maze = UnGraphMap::<Pos, usize>::new();
    maze.add_node(Pos { x: 0, y: 0 });

    mover(
        start,
        1,
        Pos { x: 0, y: 0 },
        0,
        &mut maze,
        &Info {
            start: start,
            end: end,
            walls: walls,
        },
    );

    println!("Start: {:?}, end: {:?}", &start, &end);
    let basic_dot = Dot::new(&maze);
    std::fs::write("flight_network.dot", format!("{:?}", basic_dot)).unwrap();
    print!(
        "start: {}, end: {}, ",
        maze.contains_node(start),
        maze.contains_node(end)
    );
    //let dist = dijkstra(&maze, start, Some(end), |e| *e.weight());
    let dist = astar(&maze, start, |fin| fin == end, |e| *e.weight(), |_| 0);

    println!("{:?}", dist);
    let (_, paths) = dist.unwrap();
    println!("path: {:?}", paths);

    //print maze with path
    let mut maze_copy: Vec<Vec<char>> = data.iter().map(|d| d.chars().collect()).collect();
    for p in paths {
        maze_copy[p.y][p.x] = 'x';
    }
    let maze_copy: Vec<String> = maze_copy.iter().map(|m| m.into_iter().collect()).collect();
    maze_copy.iter().for_each(|d| println!("{:?}", d));

    //println!("dist: {:?}", dist.get(&end).unwrap());
}

fn mover(
    pos: Pos,
    dir: usize,
    last_node: Pos,
    edge_total: usize,
    graph: &mut GraphMap<Pos, usize, Undirected>,
    info: &Info,
) {
    println!(
        "New Mover, pos: {:?}, dir: {}, last_node: {:?}, edge_total: {}",
        &pos.disp(),
        &dir,
        &last_node.disp(),
        &edge_total
    );
    let mut nexts: Vec<usize> = Vec::new();

    for i in 0..4 {
        if !info.walls[pos.y.wrapping_add_signed(CW[3 - i])][pos.x.wrapping_add_signed(CW[i])] {
            //dont go in reverse (2)
            if i.abs_diff(dir) != 2 {
                nexts.push(i);
            }
        }
    }
    println!("nexts: {:?}", nexts,);

    let mut last_node_new = last_node;
    let mut edge_total_new = edge_total;

    let mut fin = false;
    if graph.contains_node(pos) || nexts.len() == 0 {
        fin = true;
    }

    // create new node if reached end, or at dead end, or at junction
    if pos == info.start || pos == info.end || nexts.len() == 0 || nexts.len() > 1 {
        graph.add_node(pos);
        graph.add_edge(last_node, pos, edge_total);
        last_node_new = pos;
        edge_total_new = 0;
    }

    if fin {
        return;
    }

    for n in nexts {
        if n != dir {
            edge_total_new += 1000;
        }

        let next_pos = Pos {
            x: pos.x.wrapping_add_signed(CW[n]),
            y: pos.y.wrapping_add_signed(CW[3 - n]),
        };
        mover(next_pos, n, last_node_new, edge_total_new + 1, graph, info);
    }
}
