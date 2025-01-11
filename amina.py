def permute(array):
    result = []

    def backtrack(path, used):
        # Jika panjang path sama dengan panjang array, tambahkan ke hasil
        if len(path) == len(array):
            result.append(list(path))
            return

        # Iterasi melalui elemen array
        for i in range(len(array)):
            # Lewati elemen yang sudah digunakan
            if used[i]:
                continue

            # Tandai elemen sebagai digunakan dan tambahkan ke path
            used[i] = True
            path.append(array[i])

            # Lanjutkan eksplorasi
            backtrack(path, used)

            # Backtrack: lepaskan elemen terakhir dan tandai sebagai tidak digunakan
            path.pop()
            used[i] = False

    # Awali dengan path kosong dan semua elemen belum digunakan
    backtrack([], [False] * len(array))
    return result

# Contoh input
array = [1, 2, 3, 4, 5]

# Panggil fungsi dan tampilkan hasil
result = permute(array)
print("Semua permutasi dari", array, ":", result)