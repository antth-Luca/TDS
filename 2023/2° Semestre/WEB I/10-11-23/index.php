<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calc. Holerite</title>
    <link rel="shortcut icon" href="https://cdn.icon-icons.com/icons2/317/PNG/512/calculator-icon_34473.png" type="image/x-icon">
</head>
<body>
    <form action="processar.php">
        <div class="row mb-3">
            <div class="col-sm-8">
                <h1>Calculadora de holerite</h1>
            </div>
        </div>

        <div class="row mb-3">
            <div class="col">
                <input type="text" name="rz-social" placeholder="Razão social">
            </div>
        </div>

        <div class="row mb-3">
            <div class="col">
                <input type="text" name="cnpj" placeholder="CNPJ">
            </div>
        </div>

        <div class="row mb-3">
            <input type="text" name="nm-funcion" placeholder="Nome do funcionário">
        </div>

        <div class="row mb-3">
            <input type="text" name="func" placeholder="Função">
        </div>

        <div class="row mb-3">
            <input type="text" name="dias" placeholder="Dias de trabalho">
        </div>

        <div class="row mb-3">
            <input type="month" name="data">
        </div>

        <div class="row mb-3">
            <input type="text" name="sal-base" placeholder="Salário base">
        </div>

        <div class="row mb-3">
            <button>Calcular</button>
        </div>
    </form>

    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
</body>
</html>