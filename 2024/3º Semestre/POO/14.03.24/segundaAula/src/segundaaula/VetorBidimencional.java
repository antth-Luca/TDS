package segundaaula;
/*
 * @author ALUNO-0712
 */
public class VetorBidimencional {
    public static void main(String[] args) {
        int l=2, c=3;
        int vb[][] = new int [l][c];
        int c1, c2;
        
        for(c1 = 0; c1 < l; c1++) {
            for(c2 = 0; c2 < c; c2++) {
                vb[c1][c2] = (c1 + 1) * (c2 + 1);
            }
        }
        
        for(c1 = 0; c1 < l; c1++) {
            for(c2 = 0; c2 < c; c2++) {
                System.out.print(vb[c1][c2]);
            }
            
            System.out.println("");
        }
    }
}
