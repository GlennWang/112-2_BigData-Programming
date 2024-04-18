"""
題目：4
已知依替代式密碼(Substitution Cipher)表如下，
code_table = 
a->y
b->k
c->x
d->r
e->i
f->q
g->m
h->o
i->f
j->n
k->c
l->z
m->e
n->g
o->l
p->v
q->u
r->a
s->h
t->s
u->j
v->d
w->p
x->w
y->t
z->b


今有一段訊息，經該上述表格轉換後的結果如下:
codes = "vayxsfxi eycih viaqixs"。
請寫一 Python 程式來還原原本的訊息。 
"""
code_table = """
a->y
b->k
c->x
d->r
e->i
f->q
g->m
h->o
i->f
j->n
k->c
l->z
m->e
n->g
o->l
p->v
q->u
r->a
s->h
t->s
u->j
v->d
w->p
x->w
y->t
z->b
"""

def decode_message(codes, code_table):
    # 將密碼表轉換為字典
    substitution_dict = {}
    lines = code_table.strip().split("\n")
    for line in lines:
        key, value = line.split("->")
        substitution_dict[value.strip()] = key.strip()

    # 解密訊息
    decoded_message = ""
    for char in codes:
        if char == ' ':
            decoded_message += ' '
        else:
            decoded_message += substitution_dict[char]

    return decoded_message

# 原始訊息
codes = "vayxsfxi eycih viaqixs"

# 解密並印出結果
decoded_message = decode_message(codes, code_table)
print("原本的訊息:", decoded_message)
