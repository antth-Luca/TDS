<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gerando holerite...</title>
</head>
<body>
    <?php
        $razao = $_REQUEST['rz-social'];
        $cnpj = $_REQUEST['cnpj'];
        $nome = $_REQUEST['nm-funcion'];
        $funcao = $_REQUEST['func'];
        $dias = $_REQUEST['dias'];
        $data = $_REQUEST['data'];
        $salBase = $_REQUEST['sal-base'];
        $inss = 0;

        if($salBase <= 1320) {
            $inss = $salBase * 7.5 / 100;
        } else if($salBase <= 2571.29) {
            $inss = $salBase * 9 / 100;
        } else if($salBase <= 3856.94) {
            $inss = $salBase * 12 / 100;
        } else if($salBase <= 7504.49) {
            $inss = $salBase * 14 / 100;
        } else {
            $inss = $salBase * 20 / 100;
        }

        $descont = $salBase - $inss;
        $irrf = 0;

        if($descont >= 2142.01 & $descont <= 2826.66) {
            $irrf = $descont * 7.5 / 100;
        } else if($descont <= 3751.06) {
            $irrf = $descont * 15 / 100;
        } else if($descont <= 4664.68) {
            $irrf = $descont * 22.5 / 100;
        } else {
            $irrf = $descont * 27.5 / 100;
        }

        $liquido = $descont - $irrf;
    ?>

    <table>
        <tr colspan="2">
            <th>Recibo de pagamento de salário</th>
        </tr>
        <tr>
            <td>EMPREGADOR: <?=$razao?></td>
            <td>CNPJ: <?=$cnpj?></td>
        </tr>
    </table>
</body>
</html>