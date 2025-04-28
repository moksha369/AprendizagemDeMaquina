from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, accuracy_score
import numpy as np

# 1. Carregar o conjunto de dados Íris
iris = load_iris()
X = iris.data  # Características: [comprimento_sépala, largura_sépala, comprimento_pétala, largura_pétala]
y = iris.target  # Rótulos: 0=setosa, 1=versicolor, 2=virginica
target_names = iris.target_names  # Nomes das espécies

# 2. Dividir os dados em conjuntos de treino (80%) e teste (20%)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, 
    test_size=0.2, 
    random_state=42,  # semente para reprodutibilidade
    stratify=y  # mantém a proporção das classes
)

# 3. Criar e configurar o estimador KNN com 3 vizinhos
knn_model = KNeighborsClassifier(
    n_neighbors=3,  # número de vizinhos a considerar
    weights='uniform',  # todos os vizinhos têm igual peso
    algorithm='auto'  # o sklearn escolhe o melhor algoritmo
)

# 4. Treinar o modelo com os dados de treino
knn_model.fit(X_train, y_train)

# 5. Avaliar o modelo nos dados de teste
y_pred = knn_model.predict(X_test)

# métricas de avaliação
print("\nRelatório de Classificação:")
print(classification_report(y_test, y_pred, target_names=target_names))
print(f"Acurácia: {accuracy_score(y_test, y_pred):.2f}")

# 6. interação com o usuário
def classificar_flor():
    print("\nDigite as características da flor Íris:")
    try:
        sep_len = float(input("Comprimento da sépala (cm): "))
        sep_wid = float(input("Largura da sépala (cm): "))
        pet_len = float(input("Comprimento da pétala (cm): "))
        pet_wid = float(input("Largura da pétala (cm): "))
        
        # Criar array numpy com as características
        nova_flor = np.array([[sep_len, sep_wid, pet_len, pet_wid]])
        
        # Fazer a previsão
        predicao = knn_model.predict(nova_flor)
        probabilidades = knn_model.predict_proba(nova_flor)[0]
        
        # Mostrar resultados
        especie = target_names[predicao][0]
        print(f"\nEspécie prevista: {especie.capitalize()}")
        print("Probabilidades:")
        for i, prob in enumerate(probabilidades):
            print(f"{target_names[i]}: {prob:.2%}")
            
    except ValueError:
        print("Erro: Por favor, insira valores numéricos válidos.")

# Executar a classificação
classificar_flor()