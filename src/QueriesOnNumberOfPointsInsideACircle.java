public class QueriesOnNumberOfPointsInsideACircle {
    public static int[] countPoints(int[][] points, int[][] queries) {
        int pointsN = points.length;
        //number of points.
        int queriesN = queries.length;
        //number of queries.
        int[] answers = new int[queriesN];
        //answer array with number of points for each queries
        int crrCounter = 0;
        //counter for the current number of point for each query.
        for (int i = 0; i < queriesN; i++) {
            crrCounter = 0;
            //for each queries it repeats.
            for (int j = 0; j < pointsN; j++) {
                //for each points, check if points belong to the current circle.
                //if the distance between the point and the center of the circle
                //is equal to or smaller than the radius r, that point belongs to the circle.
                if (Math.abs(queries[i][0] - points[j][0]) <= queries[i][2]
                        && Math.abs(queries[i][1] - points[j][1]) <= queries[i][2]) {
                    crrCounter++;
                }
            }
            System.out.println(crrCounter);
            answers[i] = crrCounter;
        }
        //structure of the points: points[i] and points[1].
        return answers;
    }
    public static void main(String[]args) {
        int[][]points = new int[4][4];
        points[0][0] = 1;
        points[0][1] = 3;
        points[1][0] = 3;
        points[1][1] = 3;
        points[2][0] = 5;
        points[2][1] = 3;
        points[3][0] = 2;
        points[3][1] = 2;
        //points[4][0] = 1;
        //points[4][1] = 1;
        int[][] queries = new int[3][3];
        queries[0][0] = 2;
        queries[0][1] = 3;
        queries[0][2] = 1;

        queries[1][0] = 4;
        queries[1][1] = 3;
        queries[1][2] = 1;

        queries[2][0] = 1;
        queries[2][1] = 1;
        queries[2][2] = 2;
        countPoints(points, queries);

    }
}
