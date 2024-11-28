$(document).ready(function () {
    loadProducts();

    $('#search-btn').click(function () {
        var promocode = $('#search-input').val();
        loadProducts(promocode);
    });

    function loadProducts(promocode = null) {
        $.ajax({
            url: '/products/',
            method: 'GET',
            data: !promocode ? {} : {code: promocode},
            success: function (response) {
                $('#product-table tbody').empty();
                response.products.forEach(function (product) {
                    $('#product-table tbody').append(
                        `<tr>
                                <td><p>${product.name}</p></td>
                                <td><p>${product.price}</p></td>
                                <td><p><a href="/buy/${product.id}">Купить</a></p></td>
                            </tr>`
                    );
                });
            },
            error: function (error) {
                console.log('Ошибка при загрузке товаров:', error);
            }
        });
    }
});