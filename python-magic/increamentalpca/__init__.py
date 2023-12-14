import numpy as np
from sklearn.decomposition import IncrementalPCA , PCA

X = np.random.randint(0, 100, size=(1024, 100))

pca = PCA()
pca.fit(X)

incremental_pca = IncrementalPCA()
incremental_pca.fit(X)
incremental_pca.partial_fit(X)