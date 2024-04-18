from http import HTTPStatus

from django.db.models import Q
from django.http import Http404
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import *

try:

    from home.models import (
        ItemTransaksi,
        Lokasi,
        MetodePembayaran,
        Produk,
        SumberDana,
        Supplier,
        Transaksi,
        Unit,
        VarianProduk,
    )

except:
    pass


class UnitView(APIView):

    permission_classes = (IsAuthenticatedOrReadOnly,)

    def post(self, request):
        serializer = UnitSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                data={**serializer.errors, "success": False},
                status=HTTPStatus.BAD_REQUEST,
            )
        serializer.save()
        return Response(
            data={"message": "Record Created.", "success": True}, status=HTTPStatus.OK
        )

    def get(self, request, pk=None):
        if not pk:
            return Response(
                {
                    "data": [
                        UnitSerializer(instance=obj).data for obj in Unit.objects.all()
                    ],
                    "success": True,
                },
                status=HTTPStatus.OK,
            )
        try:
            obj = get_object_or_404(Unit, pk=pk)
        except Http404:
            return Response(
                data={"message": "object with given id not found.", "success": False},
                status=HTTPStatus.NOT_FOUND,
            )
        return Response(
            {"data": UnitSerializer(instance=obj).data, "success": True},
            status=HTTPStatus.OK,
        )

    def put(self, request, pk):
        try:
            obj = get_object_or_404(Unit, pk=pk)
        except Http404:
            return Response(
                data={"message": "object with given id not found.", "success": False},
                status=HTTPStatus.NOT_FOUND,
            )
        serializer = UnitSerializer(instance=obj, data=request.data, partial=True)
        if not serializer.is_valid():
            return Response(
                data={**serializer.errors, "success": False},
                status=HTTPStatus.BAD_REQUEST,
            )
        serializer.save()
        return Response(
            data={"message": "Record Updated.", "success": True}, status=HTTPStatus.OK
        )

    def delete(self, request, pk):
        try:
            obj = get_object_or_404(Unit, pk=pk)
        except Http404:
            return Response(
                data={"message": "object with given id not found.", "success": False},
                status=HTTPStatus.NOT_FOUND,
            )
        obj.delete()
        return Response(
            data={"message": "Record Deleted.", "success": True}, status=HTTPStatus.OK
        )


class SupplierView(APIView):

    permission_classes = (IsAuthenticatedOrReadOnly,)

    def post(self, request):
        serializer = SupplierSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                data={**serializer.errors, "success": False},
                status=HTTPStatus.BAD_REQUEST,
            )
        serializer.save()
        return Response(
            data={"message": "Record Created.", "success": True}, status=HTTPStatus.OK
        )

    def get(self, request, pk=None):
        if not pk:
            return Response(
                {
                    "data": [
                        SupplierSerializer(instance=obj).data
                        for obj in Supplier.objects.all()
                    ],
                    "success": True,
                },
                status=HTTPStatus.OK,
            )
        try:
            obj = get_object_or_404(Supplier, pk=pk)
        except Http404:
            return Response(
                data={"message": "object with given id not found.", "success": False},
                status=HTTPStatus.NOT_FOUND,
            )
        return Response(
            {"data": SupplierSerializer(instance=obj).data, "success": True},
            status=HTTPStatus.OK,
        )

    def put(self, request, pk):
        try:
            obj = get_object_or_404(Supplier, pk=pk)
        except Http404:
            return Response(
                data={"message": "object with given id not found.", "success": False},
                status=HTTPStatus.NOT_FOUND,
            )
        serializer = SupplierSerializer(instance=obj, data=request.data, partial=True)
        if not serializer.is_valid():
            return Response(
                data={**serializer.errors, "success": False},
                status=HTTPStatus.BAD_REQUEST,
            )
        serializer.save()
        return Response(
            data={"message": "Record Updated.", "success": True}, status=HTTPStatus.OK
        )

    def delete(self, request, pk):
        try:
            obj = get_object_or_404(Supplier, pk=pk)
        except Http404:
            return Response(
                data={"message": "object with given id not found.", "success": False},
                status=HTTPStatus.NOT_FOUND,
            )
        obj.delete()
        return Response(
            data={"message": "Record Deleted.", "success": True}, status=HTTPStatus.OK
        )


class ProdukView(APIView):

    permission_classes = (IsAuthenticatedOrReadOnly,)

    def post(self, request):
        serializer = ProdukSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                data={**serializer.errors, "success": False},
                status=HTTPStatus.BAD_REQUEST,
            )
        serializer.save()
        return Response(
            data={"message": "Record Created.", "success": True}, status=HTTPStatus.OK
        )

    def get(self, request, pk=None):
        if not pk:
            return Response(
                {
                    "data": [
                        ProdukSerializer(instance=obj).data
                        for obj in Produk.objects.all()
                    ],
                    "success": True,
                },
                status=HTTPStatus.OK,
            )
        try:
            obj = get_object_or_404(Produk, pk=pk)
        except Http404:
            return Response(
                data={"message": "object with given id not found.", "success": False},
                status=HTTPStatus.NOT_FOUND,
            )
        return Response(
            {"data": ProdukSerializer(instance=obj).data, "success": True},
            status=HTTPStatus.OK,
        )

    def put(self, request, pk):
        try:
            obj = get_object_or_404(Produk, pk=pk)
        except Http404:
            return Response(
                data={"message": "object with given id not found.", "success": False},
                status=HTTPStatus.NOT_FOUND,
            )
        serializer = ProdukSerializer(instance=obj, data=request.data, partial=True)
        if not serializer.is_valid():
            return Response(
                data={**serializer.errors, "success": False},
                status=HTTPStatus.BAD_REQUEST,
            )
        serializer.save()
        return Response(
            data={"message": "Record Updated.", "success": True}, status=HTTPStatus.OK
        )

    def delete(self, request, pk):
        try:
            obj = get_object_or_404(Produk, pk=pk)
        except Http404:
            return Response(
                data={"message": "object with given id not found.", "success": False},
                status=HTTPStatus.NOT_FOUND,
            )
        obj.delete()
        return Response(
            data={"message": "Record Deleted.", "success": True}, status=HTTPStatus.OK
        )


class LokasiView(APIView):

    permission_classes = (IsAuthenticatedOrReadOnly,)

    def post(self, request):
        serializer = LokasiSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                data={**serializer.errors, "success": False},
                status=HTTPStatus.BAD_REQUEST,
            )
        serializer.save()
        return Response(
            data={"message": "Record Created.", "success": True}, status=HTTPStatus.OK
        )

    def get(self, request, pk=None):
        if not pk:
            return Response(
                {
                    "data": [
                        LokasiSerializer(instance=obj).data
                        for obj in Lokasi.objects.all()
                    ],
                    "success": True,
                },
                status=HTTPStatus.OK,
            )
        try:
            obj = get_object_or_404(Lokasi, pk=pk)
        except Http404:
            return Response(
                data={"message": "object with given id not found.", "success": False},
                status=HTTPStatus.NOT_FOUND,
            )
        return Response(
            {"data": LokasiSerializer(instance=obj).data, "success": True},
            status=HTTPStatus.OK,
        )

    def put(self, request, pk):
        try:
            obj = get_object_or_404(Lokasi, pk=pk)
        except Http404:
            return Response(
                data={"message": "object with given id not found.", "success": False},
                status=HTTPStatus.NOT_FOUND,
            )
        serializer = LokasiSerializer(instance=obj, data=request.data, partial=True)
        if not serializer.is_valid():
            return Response(
                data={**serializer.errors, "success": False},
                status=HTTPStatus.BAD_REQUEST,
            )
        serializer.save()
        return Response(
            data={"message": "Record Updated.", "success": True}, status=HTTPStatus.OK
        )

    def delete(self, request, pk):
        try:
            obj = get_object_or_404(Lokasi, pk=pk)
        except Http404:
            return Response(
                data={"message": "object with given id not found.", "success": False},
                status=HTTPStatus.NOT_FOUND,
            )
        obj.delete()
        return Response(
            data={"message": "Record Deleted.", "success": True}, status=HTTPStatus.OK
        )


class MetodePembayaranView(APIView):

    permission_classes = (IsAuthenticatedOrReadOnly,)

    def post(self, request):
        serializer = MetodePembayaranSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                data={**serializer.errors, "success": False},
                status=HTTPStatus.BAD_REQUEST,
            )
        serializer.save()
        return Response(
            data={"message": "Record Created.", "success": True}, status=HTTPStatus.OK
        )

    def get(self, request, pk=None):
        if not pk:
            return Response(
                {
                    "data": [
                        MetodePembayaranSerializer(instance=obj).data
                        for obj in MetodePembayaran.objects.all()
                    ],
                    "success": True,
                },
                status=HTTPStatus.OK,
            )
        try:
            obj = get_object_or_404(MetodePembayaran, pk=pk)
        except Http404:
            return Response(
                data={"message": "object with given id not found.", "success": False},
                status=HTTPStatus.NOT_FOUND,
            )
        return Response(
            {"data": MetodePembayaranSerializer(instance=obj).data, "success": True},
            status=HTTPStatus.OK,
        )

    def put(self, request, pk):
        try:
            obj = get_object_or_404(MetodePembayaran, pk=pk)
        except Http404:
            return Response(
                data={"message": "object with given id not found.", "success": False},
                status=HTTPStatus.NOT_FOUND,
            )
        serializer = MetodePembayaranSerializer(
            instance=obj, data=request.data, partial=True
        )
        if not serializer.is_valid():
            return Response(
                data={**serializer.errors, "success": False},
                status=HTTPStatus.BAD_REQUEST,
            )
        serializer.save()
        return Response(
            data={"message": "Record Updated.", "success": True}, status=HTTPStatus.OK
        )

    def delete(self, request, pk):
        try:
            obj = get_object_or_404(MetodePembayaran, pk=pk)
        except Http404:
            return Response(
                data={"message": "object with given id not found.", "success": False},
                status=HTTPStatus.NOT_FOUND,
            )
        obj.delete()
        return Response(
            data={"message": "Record Deleted.", "success": True}, status=HTTPStatus.OK
        )


class TransaksiView(APIView):

    permission_classes = (IsAuthenticatedOrReadOnly,)

    def post(self, request):
        serializer = TransaksiSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                data={**serializer.errors, "success": False},
                status=HTTPStatus.BAD_REQUEST,
            )
        serializer.save()
        return Response(
            data={"message": "Record Created.", "success": True}, status=HTTPStatus.OK
        )

    def get(self, request, pk=None):
        if not pk:
            return Response(
                {
                    "data": [
                        TransaksiSerializer(instance=obj).data
                        for obj in Transaksi.objects.all()
                    ],
                    "success": True,
                },
                status=HTTPStatus.OK,
            )
        try:
            obj = get_object_or_404(Transaksi, pk=pk)
        except Http404:
            return Response(
                data={"message": "object with given id not found.", "success": False},
                status=HTTPStatus.NOT_FOUND,
            )
        return Response(
            {"data": TransaksiSerializer(instance=obj).data, "success": True},
            status=HTTPStatus.OK,
        )

    def put(self, request, pk):
        try:
            obj = get_object_or_404(Transaksi, pk=pk)
        except Http404:
            return Response(
                data={"message": "object with given id not found.", "success": False},
                status=HTTPStatus.NOT_FOUND,
            )
        serializer = TransaksiSerializer(instance=obj, data=request.data, partial=True)
        if not serializer.is_valid():
            return Response(
                data={**serializer.errors, "success": False},
                status=HTTPStatus.BAD_REQUEST,
            )
        serializer.save()
        return Response(
            data={"message": "Record Updated.", "success": True}, status=HTTPStatus.OK
        )

    def delete(self, request, pk):
        try:
            obj = get_object_or_404(Transaksi, pk=pk)
        except Http404:
            return Response(
                data={"message": "object with given id not found.", "success": False},
                status=HTTPStatus.NOT_FOUND,
            )
        obj.delete()
        return Response(
            data={"message": "Record Deleted.", "success": True}, status=HTTPStatus.OK
        )


class ItemTransaksiView(APIView):

    permission_classes = (IsAuthenticatedOrReadOnly,)

    def post(self, request):
        serializer = ItemTransaksiSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                data={**serializer.errors, "success": False},
                status=HTTPStatus.BAD_REQUEST,
            )
        serializer.save()
        return Response(
            data={"message": "Record Created.", "success": True}, status=HTTPStatus.OK
        )

    def get(self, request, pk=None):
        if not pk:
            return Response(
                {
                    "data": [
                        ItemTransaksiSerializer(instance=obj).data
                        for obj in ItemTransaksi.objects.all()
                    ],
                    "success": True,
                },
                status=HTTPStatus.OK,
            )
        try:
            obj = get_object_or_404(ItemTransaksi, pk=pk)
        except Http404:
            return Response(
                data={"message": "object with given id not found.", "success": False},
                status=HTTPStatus.NOT_FOUND,
            )
        return Response(
            {"data": ItemTransaksiSerializer(instance=obj).data, "success": True},
            status=HTTPStatus.OK,
        )

    def put(self, request, pk):
        try:
            obj = get_object_or_404(ItemTransaksi, pk=pk)
        except Http404:
            return Response(
                data={"message": "object with given id not found.", "success": False},
                status=HTTPStatus.NOT_FOUND,
            )
        serializer = ItemTransaksiSerializer(
            instance=obj, data=request.data, partial=True
        )
        if not serializer.is_valid():
            return Response(
                data={**serializer.errors, "success": False},
                status=HTTPStatus.BAD_REQUEST,
            )
        serializer.save()
        return Response(
            data={"message": "Record Updated.", "success": True}, status=HTTPStatus.OK
        )

    def delete(self, request, pk):
        try:
            obj = get_object_or_404(ItemTransaksi, pk=pk)
        except Http404:
            return Response(
                data={"message": "object with given id not found.", "success": False},
                status=HTTPStatus.NOT_FOUND,
            )
        obj.delete()
        return Response(
            data={"message": "Record Deleted.", "success": True}, status=HTTPStatus.OK
        )


class SumberDanaView(APIView):

    permission_classes = (IsAuthenticatedOrReadOnly,)

    def post(self, request):
        serializer = SumberDanaSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                data={**serializer.errors, "success": False},
                status=HTTPStatus.BAD_REQUEST,
            )
        serializer.save()
        return Response(
            data={"message": "Record Created.", "success": True}, status=HTTPStatus.OK
        )

    def get(self, request, pk=None):
        if not pk:
            return Response(
                {
                    "data": [
                        SumberDanaSerializer(instance=obj).data
                        for obj in SumberDana.objects.all()
                    ],
                    "success": True,
                },
                status=HTTPStatus.OK,
            )
        try:
            obj = get_object_or_404(SumberDana, pk=pk)
        except Http404:
            return Response(
                data={"message": "object with given id not found.", "success": False},
                status=HTTPStatus.NOT_FOUND,
            )
        return Response(
            {"data": SumberDanaSerializer(instance=obj).data, "success": True},
            status=HTTPStatus.OK,
        )

    def put(self, request, pk):
        try:
            obj = get_object_or_404(SumberDana, pk=pk)
        except Http404:
            return Response(
                data={"message": "object with given id not found.", "success": False},
                status=HTTPStatus.NOT_FOUND,
            )
        serializer = SumberDanaSerializer(instance=obj, data=request.data, partial=True)
        if not serializer.is_valid():
            return Response(
                data={**serializer.errors, "success": False},
                status=HTTPStatus.BAD_REQUEST,
            )
        serializer.save()
        return Response(
            data={"message": "Record Updated.", "success": True}, status=HTTPStatus.OK
        )

    def delete(self, request, pk):
        try:
            obj = get_object_or_404(SumberDana, pk=pk)
        except Http404:
            return Response(
                data={"message": "object with given id not found.", "success": False},
                status=HTTPStatus.NOT_FOUND,
            )
        obj.delete()
        return Response(
            data={"message": "Record Deleted.", "success": True}, status=HTTPStatus.OK
        )


class VarianProdukView(APIView):

    permission_classes = (IsAuthenticatedOrReadOnly,)

    def post(self, request):
        serializer = VarianProdukSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                data={**serializer.errors, "success": False},
                status=HTTPStatus.BAD_REQUEST,
            )
        serializer.save()
        return Response(
            data={"message": "Record Created.", "success": True}, status=HTTPStatus.OK
        )

    def get(self, request, pk=None):
        if not pk:
            params = request.query_params
            q = params.get("search")
            qs = VarianProduk.objects.all()

            if q:
                qs = qs.filter(Q(barcode=q) | Q(produk__nama__icontains=q))

            return Response(
                {
                    "data": [VarianProdukSerializer(instance=obj).data for obj in qs],
                    "success": True,
                },
                status=HTTPStatus.OK,
            )
        try:
            obj = get_object_or_404(VarianProduk, pk=pk)
        except Http404:
            return Response(
                data={"message": "object with given id not found.", "success": False},
                status=HTTPStatus.NOT_FOUND,
            )
        return Response(
            {"data": VarianProdukSerializer(instance=obj).data, "success": True},
            status=HTTPStatus.OK,
        )

    def put(self, request, pk):
        try:
            obj = get_object_or_404(VarianProduk, pk=pk)
        except Http404:
            return Response(
                data={"message": "object with given id not found.", "success": False},
                status=HTTPStatus.NOT_FOUND,
            )
        serializer = VarianProdukSerializer(
            instance=obj, data=request.data, partial=True
        )
        if not serializer.is_valid():
            return Response(
                data={**serializer.errors, "success": False},
                status=HTTPStatus.BAD_REQUEST,
            )
        serializer.save()
        return Response(
            data={"message": "Record Updated.", "success": True}, status=HTTPStatus.OK
        )

    def delete(self, request, pk):
        try:
            obj = get_object_or_404(VarianProduk, pk=pk)
        except Http404:
            return Response(
                data={"message": "object with given id not found.", "success": False},
                status=HTTPStatus.NOT_FOUND,
            )
        obj.delete()
        return Response(
            data={"message": "Record Deleted.", "success": True}, status=HTTPStatus.OK
        )
