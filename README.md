# simasTurbo2
 
	ROTAS:
Renderizam htmls:
‘/’ - index.html //Pagina principal
‘/manutencao’ - manutencao.html // pagina que realiza o cadastro do veículo
‘/manutencao/editar/<int:id>’ – editar.html // preenche o form com as informações do id passado e habilita a edição
Rota delete:
@app.route('/manutencao/excluir/<int:id>') // exclui o veiculo pelo id
@app.route('/manutencao/limpar') // exclui tudo da tabela manutenção
Rota update:
@app.route('/manutencao/atualizar', methods=['POST']) // rota para atualizar o cadastro, retorna url_for(‘listar’)
Rota select:
@app.route('/manutencao/visualizar/<int:id>') // visualiza a manutenção pelo id, retorna visualizar.html
@app.route('/manutencao/listar') // listar lista todas as manutenções cadastradas, retorna index.html
