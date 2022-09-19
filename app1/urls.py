from django.urls import path,include
from.import views



urlpatterns = [

    path('',views.base,name='base'),
    path('index',views.index,name='index'),
    path('group',views.group,name='group'),
    path('branch',views.branch,name='branch'),
    path('ledger',views.ledger,name='ledger'),
    path('primary',views.primary,name='primary'),
    path('costcat',views.costcat,name='costcat'),
    path('costcentr',views.costcentr,name='costcentr'),
    path('voucher',views.voucher,name='voucher'),
    path('vouchpage',views.vouchpage,name='vouchpage'),
    path('receivabl',views.receivabl,name='receivabl'),
    path('payabl',views.payabl,name='payabl'),
    path('creategroup',views.creategroup,name='creategroup'),
    path('create_group',views.create_group,name='create_group'),
    path('grcreate',views.grcreate,name='grcreate'),
    
    path('createledger',views.createledger,name='createledger'),
    path('credit',views.credit,name='credit'),
    path('debi',views.debi,name='debi'),
    path('ledgercreations',views.ledgercreations,name='ledgercreations'),
    path('ledgerlist',views.ledgerlist,name='ledgerlist'),
    path('nw',views.nw,name='nw'),
    path('groupsummery',views.groupsummery,name='groupsummery'),
    path('ledgersummary/<int:pk>',views.ledgersummary,name='ledgersummary'),
    path('ledgervoucher/<int:pk>',views.ledgervoucher,name='ledgervoucher'),

    path('voucheradd',views.voucheradd,name='voucheradd'),
    path('trialbalance',views.trialbalance,name='trialbalance'),
    path('vouchadd',views.vouchadd,name='vouchadd'),


    path('ex',views.ex,name='ex'),
    path('voucher2',views.voucher2,name='voucher2'),

    path('loanvouchadd',views.loanvouchadd,name='loanvouchadd'),
    path('voucher3',views.voucher3,name='voucher3'),

    path('cvouchadd',views.cvouchadd,name='cvouchadd'),
    path('loangroupsummary',views.loangroupsummary,name='loangroupsummary'),
    path('loanledgersummary/<int:pk>',views.loanledgersummary,name='loanledgersummary'),
    path('loanledgervoucher/<int:pk>',views.loanledgervoucher,name='loanledgervoucher'),
     path('cgroupsummary',views.cgroupsummary,name='cgroupsummary'),
    path('cgroup',views.cgroup,name='cgroup'),
    path('cledgersummary/<int:pk>',views.cledgersummary,name='cledgersummary'),
    path('cledgervoucher/<int:pk>',views.cledgervoucher,name='cledgervoucher')







    
]